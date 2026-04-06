# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        def helper(root,val):
            if not root:
                return None 
            if root.val>val:
               return  helper(root.left,val)
            elif root.val<val:
               return  helper(root.right,val)
            elif root.val==val:
                return root
        node=helper(root,val)
        return node
