class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
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
        