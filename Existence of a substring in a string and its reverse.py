class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        reverse=s[::-1]
        for i in range(len(s)-1):
            sub=s[i:i+2]
            if sub in reverse:
                return True
        return False        
