class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num))>1:
           a=0
           for i in str(num):
             a+=int(i)
             num=a
           
        return num

        