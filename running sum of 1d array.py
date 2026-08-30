class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum=0
        n=len(nums)
        res=[]
        for i in range(0,n):
            sum+=nums[i]
            res.append(sum)
        return res

        
