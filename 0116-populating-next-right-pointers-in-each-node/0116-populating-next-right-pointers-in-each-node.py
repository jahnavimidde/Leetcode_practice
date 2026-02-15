"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        q=deque()
        q.append(root)
        
        prev=None
        while q:
            prev=None
            n=len(q)
            for i in range(n):
                node=q.popleft()
                if prev is None:
                    node.next=None
                else:
                   prev.next=node
            
                if node.left:
                    q.append(node.left)
                if node.right:
                   q.append(node.right)
                prev=node
        return root
            
