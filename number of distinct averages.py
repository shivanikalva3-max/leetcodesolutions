class Solution:
    def distinctAverages(self, nums: list[int]) -> int:
        c=0
        ans=[]
        while len(nums)>0:
            a=max(nums)
            b=min(nums)
            c=(a+b)/2
            if c not in ans:
                ans.append(c)
            nums.remove(a)
            nums.remove(b)
            
        return len(ans)
                
                
        
