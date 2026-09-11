class Solution:
    def arraySign(self, nums: List[int]) -> int:
        x=1
        for i in range(0,len(nums)):
            x*=nums[i]
        if x==0:
            return 0
        elif x<0:
            return -1
        else:
            return 1
            
        
