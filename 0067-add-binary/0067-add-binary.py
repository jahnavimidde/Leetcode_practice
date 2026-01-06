class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        p=len(a)-1
        q=len(b)-1
        carry=0
        ans=""
        while p>=0 or q>=0 or carry:
            x=int(a[p]) if p>=0 else 0
            y=int(b[q]) if q>=0 else 0
            total=x+y+carry
            ans=str(total % 2)+ans
            carry=total//2
            p-=1
            q-=1
        return ans
            
        





        