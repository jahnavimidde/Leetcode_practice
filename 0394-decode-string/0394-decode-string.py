class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack=[]
        current_str=""
        current_num=0
        result=""
        for  ch in s:
            if ch.isdigit():
                current_num=current_num*10+int(ch)
            elif ch=='[':
                stack.append((current_str,current_num))
                current_str=""
                current_num=0
            elif ch==']':
                prev_str,current=stack.pop()
                current_str= prev_str+current*current_str
            else:
                current_str+=ch
        return current_str
            