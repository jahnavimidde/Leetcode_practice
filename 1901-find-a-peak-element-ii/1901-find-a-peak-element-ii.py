class Solution:
    def findPeakGrid(self, mat: list[list[int]]) -> list[int]:
        matrix=mat
        n=len(matrix)
        m=len(matrix[0])
        low=0
        high=m-1
        def maxElem(matrix,n,m,mid):
            maxi=float('-inf')
            for i in range(n):
                if matrix[i][mid]>maxi:
                    maxi=matrix[i][mid]
                    ind=i
            return ind
                
                
        while low<=high:
            mid=(low+high)//2
            row=maxElem(matrix,n,m,mid)
            left=matrix[row][mid-1] if mid-1>=0 else -1

            right=matrix[row][mid+1] if mid+1<=m-1 else -1

            if (matrix[row][mid]>left and matrix[row][mid]>right ):
                return [row,mid]
            elif matrix[row][mid]<left:
                high=mid-1
            else:
                low=mid+1
        return [-1,-1]






        