class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words=0
        for sentence in sentences:
            x=sentence.count(" ")+1
            if(x>max_words):
                max_words=x
        return max_words
        
        
