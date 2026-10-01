class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        a=" "
        b=" "
        for i in range(0,len(word1)):
            a+=word1[i]
        for j in range(0,len(word2)):
            b+=word2[j]
        if a==b:
            return True
        return False
    
        
