class Solution(object):
    def reverseWords(self, s):
        chars = list(s)
        p = 0

        for q in range(len(chars) + 1):
            if q == len(chars) or chars[q] == " ":
                chars[p:q] = chars[p:q][::-1]
                p = q + 1

        return "".join(chars)

        
        