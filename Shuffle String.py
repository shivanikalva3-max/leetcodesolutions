class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        result=[""]*len(s)
        for i in range(0,len(indices)):
            result[indices[i]]=(s[i])
        return "".join(result)

        
