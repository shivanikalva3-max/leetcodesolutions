class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxx=0
        for i in accounts:
            x=sum(i)
            if x>maxx:
                maxx=x
        return maxx
        
