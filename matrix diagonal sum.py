class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        sums=0
        n=len(mat)
        for i in range(0,len(mat)):
            for j in range(0,len(mat)):
                if i==j or j==n-i-1:
                    sums+=mat[i][j]
        return sums
        
