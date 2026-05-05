class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> st(nums.begin(),nums.end());
        int res=0;
        for(auto num:st)
        {
            if(st.find(num-1)==st.end())
            {
                int streak=1;
                while(st.find(num+streak)!=st.end())
                {
                    streak++;
                }
                res=max(res,streak);
            }
        }
        return res;
    }
};
