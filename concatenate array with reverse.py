class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        arr=nums.copy()
        for i in range(len(nums)-1,-1,-1):
            arr.append(nums[i])
        return arr     
