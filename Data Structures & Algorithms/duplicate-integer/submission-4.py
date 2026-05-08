from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # seen={}
        # for num in nums:
        #     if seen[num] >1:
        #         return True
        #     seen[num]+=1
        # return False

        # st=set()
        # for num in nums:
        #     if num in st:
        #         return True
        #     st.add(num)
        # return False

        seen =defaultdict(int)
        for num in nums:
            seen[num]+=1
        for key in seen.keys():
            if seen[key]>1:
             return True
        return False
        # return len(nums)!=len(list(set(nums)))



    
    

        