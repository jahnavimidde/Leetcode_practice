# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0
        
        left=self.minDepth(root.left)
        right=self.minDepth(root.right)
        if root.left is None or root.right is None:
            return max(right,left)+1
        return min(left,right)+1
        