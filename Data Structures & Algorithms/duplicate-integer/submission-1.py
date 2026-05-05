class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp={}
        for i in nums:
            if i in mp:
                mp[i]+=1
            else:
                mp[i]=1
        
        for num,count in mp.items():

            if count>1:
                return True
        return False
        