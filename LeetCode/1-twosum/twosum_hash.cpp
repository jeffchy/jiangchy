class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // using hash table
        unordered_map<int,int>hashMap;
        vector<int>vec;
        for (int i = 0;i<nums.size();i++){
            hashMap[nums[i]] = i; // simple hash function
            // kay: value val:index
        }
        for (int j = 0;j<nums.size();j++){
            int diff = target - nums[j];
           if (hashMap.find(diff) != hashMap.end() && hashMap[diff] > j) {
                vec.push_back(j);
                vec.push_back(hashMap[diff]);
                break;
            }
        }
        return vec;
    }
};