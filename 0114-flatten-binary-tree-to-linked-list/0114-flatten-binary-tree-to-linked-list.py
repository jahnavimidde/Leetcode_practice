class Solution:
    def flatten(self, root):
        cur = root

        while cur:
            if cur.left:
                prev = cur.left

                while prev.right:
                    prev = prev.right

                prev.right = cur.right
                cur.right = cur.left
                cur.left = None

            cur = cur.right