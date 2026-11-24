class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        for num in range(1,n*n+1):
            c=0
            for i in range(n):
                for j in range(n):
                    if grid[i][j]==num:
                        c+=1
            if c==2:
                repeat=num
            if c==0:
                missing=num
        return [repeat,missing]
