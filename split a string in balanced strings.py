class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count=0
        counts=0
        countt=0
        for i in s:
            if i=='R':
                count+=1
            elif i=='L':
                counts+=1
            a=count-counts
            if a==0:
                countt+=1
        return countt


        
