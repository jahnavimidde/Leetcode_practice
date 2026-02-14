from collections import deque

class Solution(object):
    def isCousins(self, root, x, y):
        
        queue = deque([root])
        
        while queue:
            level = []
            n = len(queue)
            
            for i in range(n):
                node = queue.popleft()
                level.append(node.val)
                
                # 🔥 Check if x and y are siblings (same parent)
                if node.left and node.right:
                    if (node.left.val == x and node.right.val == y) or \
                       (node.left.val == y and node.right.val == x):
                        return False
                
                if node.left:
                    queue.append(node.left)
            
                if node.right:
                    queue.append(node.right)
            
            # 🔥 Check if both are in same level
            if x in level and y in level:
                return True
        
        return False