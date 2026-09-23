class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        n=len(matrix)
        m=len(matrix[0])
        ans = [[0] * n for _ in range(m)]
        for i in range(0,n):
            for j in range(0,m):
                ans[j][i]=matrix[i][j]
        return ans
        
