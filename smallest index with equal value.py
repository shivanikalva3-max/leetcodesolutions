class Solution:
    def smallestEqual(self, nums: list[int]) -> int:
        arr=[]
        for i in range(0,len(nums)):
            if nums[i]==i%10:
                arr.append(i)
        if len(arr)==0:
            return -1
        else:
            return min(arr)
        
                
        
