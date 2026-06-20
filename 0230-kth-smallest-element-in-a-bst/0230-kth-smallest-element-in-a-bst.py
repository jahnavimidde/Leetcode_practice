# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        
        k=[k]
        def inorder(root):
            
            if not root:
                return None  
            
            left=inorder(root.left)
            if left is not None:
                return left
                
            k[0]-=1
            if k[0]==0:
                ans=root.val
                return ans
                
            
            return inorder(root.right)
        
        ans_=inorder(root)
        return ans_
                
        