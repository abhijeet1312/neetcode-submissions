class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int,int> mp;
        for(auto i:nums)
        {
            mp[i]++;

        }
        for(auto num:mp)
        {
            if(num.second>1)
             return true;
              
        }
        return false;
    }
};