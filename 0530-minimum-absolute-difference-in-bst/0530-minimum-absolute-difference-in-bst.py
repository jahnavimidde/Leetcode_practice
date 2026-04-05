class Solution(object):
    def getMinimumDifference(self, root):
        self.prev = None
        self.min_diff = float('inf')

        def inorder(node):
            if not node:
                return
            
            inorder(node.left)

            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)
            
            self.prev = node.val

            inorder(node.right)

        inorder(root)
        return self.min_diff