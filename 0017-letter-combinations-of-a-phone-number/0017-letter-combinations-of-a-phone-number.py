class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        start=0
        map = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}
        result=self.helper(start,"",[],digits,map)
        return result
    def helper(self,start,ds,ans,digits,map):
        if len(ds)==len(digits):
            ans.append(ds[:])
            return 
        if start<len(digits):
            for i in (map[digits[start]]):
                ds+=i
                self.helper(start+1,ds,ans,digits,map)
                ds=ds[:-1]
        return ans
         
        