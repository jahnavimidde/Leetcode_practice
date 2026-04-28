class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        
        for t in tokens:
            if t in "+-*/":
                b = stack.pop()
                a = stack.pop()
                
                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(a - b)
                elif t == "*":
                    stack.append(a * b)
                else:  # division
                    # force truncate toward zero WITHOUT floats ambiguity
                    res=abs(a)//abs(b)
                    if (a<0)^(b<0):
                        res=-res
                    stack.append(res)
            else:
                stack.append(int(t))
        
        return stack[0]