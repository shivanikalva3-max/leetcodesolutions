class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        count=0
        for i in range(0,len(words1)):
            for j in range(0,len(words2)):
                if words1[i]==words2[j] and words1.count(words1[i])==1 and words2.count(words2[j])==1:
                    count+=1
        return count

        
