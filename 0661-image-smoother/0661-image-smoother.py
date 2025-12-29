class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        m=len(img)
        n=len(img[0])
        result=[[0]*n for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                sum_=0
                count=0
                for dx in [-1,0,1]:
                    for dy in [-1,0,1]:
                        i1=dx+i
                        j1=dy+j
                        if 0<=i1<m and 0<=j1<n:
                            count+=1
                            sum_ +=img[i1][j1]
                avg=sum_//count
                result[i][j]=avg
        return result 
                    



        