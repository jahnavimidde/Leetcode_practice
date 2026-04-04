# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        s=""
        ans=[]
        sum_=0
        def helper(root,curr):
            if not root:
                
                return 0
            curr=curr*10+root.val
            
            if not root.left and not root.right:
                
                return curr
            return helper(root.left,curr)+helper(root.right, curr)
        curr=helper(root,0)
        return curr
        
        

        


















        # s=""
        # ans=[]
        # sum_=0
        # def helper(root,s,ans):
        #     if not root:
                
        #         return 
            
        #     if not root.left and not root.right:
        #         s+=str(root.val)
        #         ans.append(s)
        #         return 
        #     if not root.left and root.right:
        #         right=helper(root.right,s+str(root.val),ans)
        #     if root.left and not root.right:
        #         left=helper(root.left,s+str(root.val),ans)

        #     if root.left and root.right:
        #         left=helper(root.left,s+str(root.val),ans)
                
                
        #         right=helper(root.right,s+str(root.val),ans)
        # helper(root,s,ans)
        # for i in ans:
        #     sum_+=int(i)
        # return sum_
            
            
            
           
        