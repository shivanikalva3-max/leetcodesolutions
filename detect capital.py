class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.upper()==word or word.lower()==word:
            return True
        elif word[1:]==word[1:].lower() and word[:1]==word[:1].upper():
            return True
        else:
            return False

        
        
