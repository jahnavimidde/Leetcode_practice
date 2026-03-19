# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """

        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        n=len(nums)
        mid=n//2

        root=TreeNode(nums[mid])
        parent=root
        stack=[(parent,0,mid),(parent,mid+1,n)]

        while stack:
            parent,l,h=stack.pop()
            mid=(l+h)//2
            if l<h:
                if nums[mid]<parent.val:
                    parent.left=TreeNode(nums[mid])
                    parent=parent.left
                else:
                    parent.right=TreeNode(nums[mid])
                    parent=parent.right
                stack.append((parent,l,mid))
                stack.append((parent,mid+1,h))
        return root
        