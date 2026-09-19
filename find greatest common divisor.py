class Solution:
    def findGCD(self, nums: list[int]) -> int:
        smallest=nums[0]
        greatest=nums[0]
        for i in range(1,len(nums)):
            if smallest>nums[i]:
                smallest=nums[i]
            if greatest<nums[i]:
                greatest=nums[i]
        while(greatest%smallest)!=0:
            greatest,smallest=smallest,greatest%smallest
        return smallest
        


        
