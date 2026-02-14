class Solution(object):
    def hasPathSum(self, root, targetSum):
        if root is None:
            return False
        
        return self.helper(root, targetSum, 0)

    def helper(self, root, targetSum, Sum):
        if root is None:
            return False
        
        Sum += root.val   # 🔥 Add first
        
        if root.left is None and root.right is None:
            return Sum == targetSum
        
        left = self.helper(root.left, targetSum, Sum)
        right = self.helper(root.right, targetSum, Sum)
        
        return left or right