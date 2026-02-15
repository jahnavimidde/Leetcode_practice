# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
       
        queue=deque([root])
        r=[]
        while queue:
            level=[]
            n=len(queue)
            for i in range(n):
                node=queue.popleft()
                level.append(node.val)
                if node.left:
                   queue.append(node.left)
            
                if node.right:
                   queue.append(node.right)
            r.insert(0,level)
        return r  
        