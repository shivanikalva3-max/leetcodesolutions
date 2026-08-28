class Solution:
    def countDigits(self, num: int) -> int:
        count=0
        nums=num
        while num>0:
            rem=num%10
            if(nums%rem==0):
                count+=1
            num=num//10
        return count

        
