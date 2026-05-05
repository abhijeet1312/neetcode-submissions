class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # seen={}
        # for num in nums:
        #     if seen[num] >1:
        #         return True
        #     seen[num]+=1
        # return False

        st=set()
        for num in nums:
            if num in st:
                return True
            st.add(num)
        return False


    
    

        