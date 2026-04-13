class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k==len(num):
            return "0"
        stack=[]
        i=0
        while i<=len(num)-1:
            if not stack:
                stack.append(num[i])
            else:
                while stack and stack[-1]>num[i] and k:
                    stack.pop()
                    k-=1
                stack.append(num[i])
            i+=1
        

        while k!=0:
            stack.pop()
            k-=1
        output="".join(map(str,stack)) 
        return output.lstrip('0') or '0'
        


