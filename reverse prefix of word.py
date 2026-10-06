class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        c=word.find(ch)
        a=word[0:c+1]
        b=a[::-1]
        return b+word[c+1:]
        
