class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        arr=[]
        for i in range(0,len(s),k):
            x=s[i:i+k]
            l=len(x)
            if l<k:
                x+=fill*(k-len(x))
            arr.append(x)
        return arr
