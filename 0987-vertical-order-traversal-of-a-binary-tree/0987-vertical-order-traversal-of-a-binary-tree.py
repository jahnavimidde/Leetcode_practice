# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        nodes = {}

        # Queue for BFS traversal
        from collections import deque, defaultdict
        todo = deque()
        todo.append((root, 0, 0))

        # BFS loop
        while todo:
            temp, x, y = todo.popleft()

            # Insert into dictionary
            if x not in nodes:
                nodes[x] = {}
            if y not in nodes[x]:
                nodes[x][y] = []
            nodes[x][y].append(temp.val)

            # Left child
            if temp.left:
                todo.append((temp.left, x - 1, y + 1))
            # Right child
            if temp.right:
                todo.append((temp.right, x + 1, y + 1))

        # Prepare final result
        ans = []
        for x in sorted(nodes.keys()):
            col = []
            for y in sorted(nodes[x].keys()):
                col.extend(sorted(nodes[x][y]))
            ans.append(col)

        return ans
        