# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if  not root :
            return 0
        q=deque()
        q.append((root,0))
        max_width=0
        while q:
            n=len(q)
            _,min_ind=q[0]
            for i in range(n):
                node,id=q.popleft()
                ind=id-min_ind
                if node.left:
                    q.append((node.left,2*ind+1))
                if node.right:
                    q.append((node.right,2*ind+2))
                if i==0:
                    first_ind=ind
                if i == n-1:
                    last_ind=ind
            max_width=max(max_width,last_ind-first_ind+1)
        return max_width