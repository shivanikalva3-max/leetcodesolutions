class Solution:
    def averageValue(self, nums: list[int]) -> int:
        arr=[]
        a=0
        for i in range (0,len(nums)):
            if nums[i]%3==0 and nums[i]%2==0:
                arr.append(nums[i])
        for j in range(len(arr)):
            a+=arr[j]
        if len(arr)==0:
            return 0
        return a//len(arr)

        
                
            

        
