class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        
        ans=mat
        queue=deque()
        vis=[[False]*len(mat[0]) for i in range(len(mat))]
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    queue.append((i,j,0))
                    vis[i][j]=True
        dir=[(-1,0),(0,-1),(1,0),(0,1)]      
        while queue:
            row,col,dis=queue.popleft()
            for d1,d2 in dir:
                nr=row+d1
                nc=col+d2
                # mini=float('-inf')
                if 0<=nr<len(mat) and 0<=nc<len(mat[0]) and not vis[nr][nc] :
                    
                   
                        vis[nr][nc]=True
                        ans[nr][nc]=dis+1
                        queue.append((nr,nc,dis+1))
                    
        return ans
        

                
            
