class Solution:
    def findComplement(self, num: int) -> int:
        binary=bin(num)[2:]
        rev=""
        for i in binary:
            if i=='0':
                rev+='1'
            else:
                rev+='0'
        return int(rev,2)
