from functools import cmp_to_key

class Solution(object):
    def largestNumber(self, nums):
        
        def compare(a, b):
            if a + b > b + a:
                return -1
            else:
                return 1
        
        nums_str = list(map(str, nums))
        nums_str.sort(key=cmp_to_key(compare))
        
        result = ''.join(nums_str)
        
        return "0" if result[0] == '0' else result