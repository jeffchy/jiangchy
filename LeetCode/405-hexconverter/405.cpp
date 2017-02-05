class Solution {
public:
    string toHex(int num) {
        string hex_ele[16] = {"0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"};
        string result;
        if (num == 0){result = "0";}
        else if(num > 0){
            while(num != 0){
                result += hex_ele[num & 15];
                num >>= 4;
            }
        }
        else{
            for (int i = 0;i < 8;i++){
                result += hex_ele[num & 15];
                num >>= 4;
            }
        }
        reverse(result.begin(),result.end());
        return result;
    }
};