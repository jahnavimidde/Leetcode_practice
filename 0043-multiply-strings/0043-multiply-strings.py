class Solution(object):
    def multiply(self, num1, num2):
        n1 = 0
        for i in num1:
            n1 = n1*10 + (ord(i) - 48)

        n2 = 0
        for j in num2:
            n2 = n2*10 + (ord(j) - 48)   
        
        return str(n1*n2)