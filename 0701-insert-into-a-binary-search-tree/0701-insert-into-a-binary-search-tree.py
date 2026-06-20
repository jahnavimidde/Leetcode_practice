# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        new=TreeNode(val)
        
        def insert(root):
            if not root:
                root=new
                return root
            # if not root.left and not root.right:
            #     if root.val<new.val:
            #         root.right=new
            #         return root
            #     else:
            #         root.left=new
            #         return root

            # else:
            if new.val<root.val:
                    root.left=insert(root.left)
                    return root
            elif  new.val>root.val:
                    root.right=insert(root.right)
                    return root

        root=insert(root)
        return root
        