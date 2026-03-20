# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        paths=[]
        def dfs(root,path):
            if root is None:
                return 
            if path=="":
                new_path=str(root.val)
            else:
                new_path=path+"->"+str(root.val)
            if root.left is None and root.right is None:
                paths.append(new_path)
                return 
            if root.left :
                dfs(root.left,new_path)
            if root.right:
                dfs(root.right,new_path)
        dfs(root,"")
        return paths