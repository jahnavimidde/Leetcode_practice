class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """




        if len(triangle)-1==0 and len(triangle[-1])-1==0:
                return triangle[0][0]
        # def helper(i,j):
        #     if i==0 and j==0:
        #         return triangle[i][j]
            
        #     if j==0 and i!=0:
        #             ini=triangle[i][j]+helper(i-1,j)
        #             return ini
        #     elif j==len(triangle[i])-1 and i!=0:
        #         last=triangle[i][j]+helper(i-1,j-1)
        #         return last
        #     else:
        #         mid1=triangle[i][j]+helper(i-1,j-1)
        #         mid2=triangle[i][j]+helper(i-1,j)
        #         return min(mid1,mid2)
        # m=float('inf')
        # for j in range(len(triangle[-1])):
        #     mini=helper(len(triangle)-1,j)
        #     m=min(mini,m)
        # return m



        # For the Triangle problem, interviewers usually expect the top → bottom recurrence because it's simpler:

        # helper(i,j):
        #     if i == last_row:
        #         return triangle[i][j]

        #     down = helper(i+1, j)
        #     diag = helper(i+1, j+1)

        #     return triangle[i][j] + min(down, diag)




        #SPACE OPTIMIZATION 
        n=len(triangle)
        front=[-1]*len(triangle[-1])
        for j in range(len(triangle[-1])):
            front[j]=triangle[n-1][j]
        for i in range(n-2,-1,-1):
            temp=[-1]*(i+1)
            for j in range(i+1):
                one=front[j]
                two=front[j+1]
                temp[j]=triangle[i][j]+min(one,two)
            front=temp

        return temp[0]

        





        




        
            
            

                     
        