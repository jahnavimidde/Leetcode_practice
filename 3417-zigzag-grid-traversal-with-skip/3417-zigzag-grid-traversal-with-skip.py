class Solution(object):
    def zigzagTraversal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        skip= False
        rev= False
        temp=[]
        k=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not skip:
                    temp.append(grid[i][j])
                    skip= True
                else:
                    skip= False
            k+=1
            if not rev and k<len(grid):
                grid[k].reverse()
                rev= True
            else:
                rev= False
        return temp