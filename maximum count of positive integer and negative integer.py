class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        count=0
        countt=0
        for i in range(0,len(nums)):
            if nums[i]>0:
                count+=1
            if nums[i]<0:
                countt+=1
        return max(count,countt)
