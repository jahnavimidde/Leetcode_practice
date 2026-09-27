class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        #we need a start where it can have desc and asc order (comaparison posiblity)

        row=0
        col=len(matrix[0])-1
        while row<len(matrix) and col>=0:
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]<target:
                #eliminate row
                row+=1
            else:
                #eliminate col
                col-=1    #because if that ele is greater then next elements down to is also greater
        return False

        