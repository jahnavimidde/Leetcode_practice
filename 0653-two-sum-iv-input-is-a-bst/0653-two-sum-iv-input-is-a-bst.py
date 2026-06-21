# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        if root is None:
            return False
        if root.left is None and root.right is None:
            return False
        q=deque()
        q.append(root)
        def hasnode(root,new,curr):
            if root is None:
                return False
            if root.val==new:
                return root!=curr 
            elif new<root.val:
                return hasnode(root.left,new,curr)
            elif new>root.val:
                return hasnode(root.right,new,curr)
        while q:
            node=q.popleft()
            value=k-node.val
            
            if hasnode(root,value,node):
                return True 
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return False
            
            

            
        