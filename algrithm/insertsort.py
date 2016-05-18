#input type
#6
#1 4 5 3 2 1

size = int(input().strip())
arr = input().strip().split()
arr = [int(i) for i in arr]
for k in range(1,size):
    temp = arr[k]
    for i in range(k - 1,-1,-1):
        if arr[i] > temp:
            #print(' '.join([str(j) for j in arr]))
            arr[i+1] = arr[i]
            arr[i] = temp
        elif arr[i] < temp:
            #print(' '.join([str(j) for j in arr]),111)
            arr[i+1] = temp
            break
    print(' '.join([str(j) for j in arr]))