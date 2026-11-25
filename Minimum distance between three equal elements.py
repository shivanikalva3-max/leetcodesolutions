class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        res = 10 ** 9
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] == nums[j] == nums[k]:
                        res = min(res, abs(i - j) + abs(j - k) + abs(k - i))
        if res == 10 ** 9:
            return -1
        else:
            return res
