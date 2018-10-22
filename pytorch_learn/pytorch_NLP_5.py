import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

################################################
### char-level representation augmented TAGGER #
################################################


torch.manual_seed(1)
CHAR_HIDDEN_DIM = 5

training_data = [
    ("The dog ate the apple".split(), ["DET", "NN", "V", "DET", "NN"]),
    ("Everybody read that book".split(), ["NN", "V", "DET", "NN"])
]

# prepare for the char-level embedding
char_to_idx = {}
for sent, _ in training_data:
    for word in sent:
        for char in word:
            if char not in char_to_idx:
                char_to_idx[char] = len(char_to_idx)
print(char_to_idx)

# make the input of char
char_to_onehot = {}
for char, idx in char_to_idx.items():
    one_hot = torch.zeros(len(char_to_idx))
    one_hot[idx] = 1
    char_to_onehot[char] = one_hot

# construct the char-level input for each word
class LSTMchar(nn.Module):

    def __init__(self, char_input_dim, char_hidden_dim):
        super(LSTMchar, self).__init__()
        self.char_input_dim = char_input_dim
        self.char_hidden_dim = char_hidden_dim
        self.hidden = self.init_hidden()
        self.lstm = nn.LSTM(self.char_input_dim, self.char_hidden_dim)


    def init_hidden(self):
        return (torch.zeros(1, 1, self.char_hidden_dim),
                torch.zeros(1, 1, self.char_hidden_dim))

    def forward(self, word, char_to_onehot):
        embeds = tuple([char_to_onehot[char] for char in word])
        embeds = torch.cat(embeds)

        lstm_out, self.hidden = self.lstm(
            embeds.view(len(word), 1, -1), self.hidden)

        return lstm_out[-1][0]

model = LSTMchar(len(char_to_onehot), CHAR_HIDDEN_DIM)
char_hidden = model('dog', char_to_onehot)

# prepare for the word embedding
word_to_char_embedding = {}
word_to_ix = {}
for sent, tags in training_data:
    for word in sent:
        if word not in word_to_ix:
            word_to_ix[word] = len(word_to_ix)
            with torch.no_grad():
                word_to_char_embedding[word] = model(word, char_to_onehot)


print(word_to_ix)
print(word_to_char_embedding)
tag_to_ix = {"DET": 0, "NN": 1, "V": 2}

# These will usually be more like 32 or 64 dimensional.
# We will keep them small, so we can see how the weights change as we train.
EMBEDDING_DIM = 6
HIDDEN_DIM = 6

class LSTMTagger(nn.Module):

    def __init__(self, embedding_dim, char_hidden_dim, hidden_dim, vocab_size, tagset_size):
        super(LSTMTagger, self).__init__()
        self.hidden_dim = hidden_dim

        self.word_embeddings = nn.Embedding(vocab_size, embedding_dim)

        # The LSTM takes word embeddings as inputs, and outputs hidden states
        # with dimensionality hidden_dim.
        self.lstm = nn.LSTM(embedding_dim + char_hidden_dim, hidden_dim)

        # The linear layer that maps from hidden state space to tag space
        self.hidden2tag = nn.Linear(hidden_dim, tagset_size)
        self.hidden = self.init_hidden()

    def init_hidden(self):
        # Before we've done anything, we dont have any hidden state.
        # Refer to the Pytorch documentation to see exactly
        # why they have this dimensionality.
        # The axes semantics are (num_layers, minibatch_size, hidden_dim)
        return (torch.zeros(1, 1, self.hidden_dim),
                torch.zeros(1, 1, self.hidden_dim))

    def forward(self, sentence, word_to_ix, word_to_char_embedding):
        _temp = []
        for word in sentence:
            word_embeds = self.word_embeddings(torch.tensor(word_to_ix[word], dtype=torch.long))
            word_char_level_embeds = word_to_char_embedding[word]
            _temp.append(word_embeds)
            _temp.append(word_char_level_embeds)

        embeds = torch.cat(_temp)
        lstm_out, self.hidden = self.lstm(
            embeds.view(len(sentence), 1, -1), self.hidden)
        tag_space = self.hidden2tag(lstm_out.view(len(sentence), -1))
        tag_scores = F.log_softmax(tag_space, dim=1)
        return tag_scores


model = LSTMTagger(EMBEDDING_DIM, CHAR_HIDDEN_DIM, HIDDEN_DIM, len(word_to_ix), len(tag_to_ix))
loss_function = nn.NLLLoss()
optimizer = optim.SGD(model.parameters(), lr=0.1)


def prepare_sequence(seq, to_ix):
    idxs = [to_ix[w] for w in seq]
    return torch.tensor(idxs, dtype=torch.long)

# See what the scores are before training
# Note that element i,j of the output is the score for tag j for word i.
# Here we don't need to train, so the code is wrapped in torch.no_grad()

######## THIS IS IMPORTANT #########
with torch.no_grad():
######## WE JUST WANT TO EVALUATE THE DATA #####

    tag_scores = model(training_data[0][0], word_to_ix, word_to_char_embedding)
    print(tag_scores)

for epoch in range(300):  # again, normally you would NOT do 300 epochs, it is toy data
    for sentence, tags in training_data:
        # Step 1. Remember that Pytorch accumulates gradients.
        # We need to clear them out before each instance
        model.zero_grad()

        # Also, we need to clear out the hidden state of the LSTM,
        # detaching it from its history on the last instance.
        model.hidden = model.init_hidden()

        # Step 3. Run our forward pass.
        tag_scores = model(sentence, word_to_ix, word_to_char_embedding)

        # Step 4. Compute the loss, gradients, and update the parameters by
        #  calling optimizer.step()
        loss = loss_function(tag_scores, prepare_sequence(tags, tag_to_ix))
        loss.backward()
        optimizer.step()

# See what the scores are after training
with torch.no_grad():
    tag_scores = model(training_data[0][0], word_to_ix, word_to_char_embedding)

    # The sentence is "the dog ate the apple".  i,j corresponds to score for tag j
    # for word i. The predicted tag is the maximum scoring tag.
    # Here, we can see the predicted sequence below is 0 1 2 0 1
    # since 0 is index of the maximum value of row 1,
    # 1 is the index of maximum value of row 2, etc.
    # Which is DET NOUN VERB DET NOUN, the correct sequence!
    print(tag_scores)