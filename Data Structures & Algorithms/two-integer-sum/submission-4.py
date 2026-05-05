class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        ans=0
        for i,num in enumerate(nums) :
            if target-num in seen:
                ans= [seen[target-num],i]
            seen[num]=i
        return ans
    
            
       
      
        