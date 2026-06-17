class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        def helper(heights):
        
            st=deque()
            max_area=0
            for i in range(len(heights)):
                while st and heights[st[-1]]>heights[i]:
                    ele=st[-1]
                    st.pop()
                    nse=i
                    if not st:
                        pse=-1
                    else:
                        pse=st[-1]
                    max_area=max(max_area,heights[ele]*(nse-pse-1))
                st.append(i)
            while st:
                ele=st[-1]
                st.pop()
                nse=len(heights)
                if not st:
                    pse=-1
                else:
                    pse=st[-1]

                max_area=max(max_area,heights[ele]*(nse-pse-1))
            return max_area
        max_area=0
        if not matrix or not matrix[0]:
            return 0
        heights=[0]*len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=="1":
                    heights[j]+=1
                else:
                    heights[j]=0
            area=helper(heights)
            max_area=max(max_area,area)
        return max_area