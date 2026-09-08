class Solution:
    def fib(self, n: int) -> int:
        a=0
        b=1
        while n>0:
            c=a+b
            n-=1
            a=b
            b=c
        return a
        
