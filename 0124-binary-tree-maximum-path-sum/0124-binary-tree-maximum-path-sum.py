# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.maxi=float('-inf')
        
        def helper(root):
            if not root:
             return 0
            leftsum=max(0,helper(root.left))
            rightsum=max(0,helper(root.right))
            self.maxi=max(self.maxi,root.val+leftsum+rightsum)
            return root.val+max(leftsum,rightsum)
        helper(root)
        return self.maxi
        
        
            
        
    
        