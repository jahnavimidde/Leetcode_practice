class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack=[]
        NGE={}
        for num in reversed(nums2):
            while  stack and stack[-1]<=num:
                stack.pop()
            if not stack:
                NGE[num]=-1
            else:
                NGE[num]=stack[-1]
            stack.append(num)
        result=[]
        for num in nums1:
            result.append(NGE[num])
        return result