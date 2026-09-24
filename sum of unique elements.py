class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        sums=0
        for i in range(0,len(nums)):
            count=0
            for j in range(0,len(nums)):
                if nums[i]==nums[j]:
                    count+=1
            if count==1:
                sums+=nums[i]
        return sums
        
