#include <vector>
#include <iostream>
using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        // in a violent way
        vector<int>vec;
        for (int i = 0;i<nums.size();i++){
            int temp = nums[i];
            for (int j = (i+1);j<nums.size();j++){
                if (temp + nums[j] == target){ // check the next else O(n2)
                    vec.push_back(i);
                    vec.push_back(j);
                    break;
                }
            }
        }
        return vec;
    }
};


