class Solution(object):
    def myAtoi(self, s):
        mini = -2**31
        maxi = 2**31 - 1

        i = 0
        n = len(s)

        # skip spaces
        while i < n and s[i] == " ":
            i += 1

        # sign
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        num = 0
        ans = self.helper(s, i, sign, num, mini, maxi)
        return max(mini, min(maxi, ans))

    def helper(self, s, i, sign, num, mini, maxi):
        # base case
        if i >= len(s) or not s[i].isdigit():
            return sign * num

        # build number
        num = num * 10 + int(s[i])

        # overflow check
        if sign * num > maxi:
            return maxi
        if sign * num < mini:
            return mini

        return self.helper(s, i + 1, sign, num, mini, maxi)
