from collections import Counter 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        top=(freq.most_common())
        print(top)
        baba=[]
        ans=[]
        for i in range(0,k):
            ans.append(top[i][0])
        return ans
        


        