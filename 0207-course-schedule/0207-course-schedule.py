class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if len(prerequisites)==1 and prerequisites[0][0]!=prerequisites[0][1]:
            return True
        adj={i:[] for i in range(0,numCourses)}
        for i in prerequisites:
            u,v=i
            adj[v].append(u)
        vis=[0]*(numCourses)
        path=[0]*(numCourses)
        def dfs(u):
            vis[u]=1
            path[u]=1
            
            for nei in adj[u]:
                if vis[nei]==0:
                    if dfs(nei):
                        return True
                elif path[nei]==1:
                    return True
            path[u]=0
            return False           
        for i in range(0,numCourses):
            if vis[i]==0:
                cycle=dfs(i)
                if cycle:
                    return False
        return True
                
            




        