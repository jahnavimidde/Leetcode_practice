class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]
        else:
            row=[[1],[1,1]]
            
            for i in range(2,rowIndex+1):
                re=[1]
                for j in range(len(row[i-1])-1):
                    val=row[i-1][j]+row[i-1][j+1]
                    re.append(val)
                re.append(1)
                row.append(re)
            return row[rowIndex]
            
        