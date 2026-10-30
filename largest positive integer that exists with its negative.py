class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        a=-1
        maxx=-1
        for i in nums:
            if i>0 and -i in nums:
                a=i
                if a>maxx:
                    maxx=a
        return maxx


        
