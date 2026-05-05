class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #sorting based

        A=[]

        for i,num in enumerate(nums):
            A.append([num,i])

        A.sort()

        i,j=0,len(nums)-1

        while i<j:
            curr_sum=A[i][0]+A[j][0]
            if curr_sum==target:
                return [min(A[i][1],A[j][1]),
                max(A[i][1],A[j][1])]
            elif curr_sum<target:
                i+=1
            else:
                j-=1

        return []

        