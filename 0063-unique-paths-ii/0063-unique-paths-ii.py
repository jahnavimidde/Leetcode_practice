class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        prev=[0]*n
        for i in range(m):
            temp=[-1 for _ in range(n)]
            for j in range(n):
                if obstacleGrid[i][j]==1:
                    temp[j]=0
                
                elif i==0 and j==0:
                    temp[j]=1 #there is only one way to reach the start
                else:
                    above=prev[j] 
                    pre=temp[j-1] if j>0 else 0
                    temp[j]=above+pre
            prev=temp
        return temp[n-1]
        