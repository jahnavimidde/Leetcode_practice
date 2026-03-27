class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n==1:
            return [0]
        adj={i:[] for i in range(0,n)}
        deg=[0]*n
        
        remaining_nodes=n
        for edge in edges:
            u,v=edge[0],edge[1]
            adj[u].append(v)
            deg[u]+=1
            adj[v].append(u)
            deg[v]+=1
        q=deque()
        for i in range(0,n):
            if deg[i]==1:
                q.append(i)
        while q:
            size=len(q)
            # if size<=2:
            #     break
            if remaining_nodes<=2:
                break
            
            for _ in range(size):
                curr=q.popleft()
                for nei in adj[curr]:
                    deg[nei]-=1
                    if deg[nei]==1:
                        q.append(nei)
            remaining_nodes-=size
    
        return list(q)


        
    
            