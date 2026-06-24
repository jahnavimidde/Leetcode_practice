class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        if image[sr][sc]==color:
            return image 
        queue=deque()
        old=image[sr][sc]
        queue.append((sr,sc,old))
        while queue:
            sr,sc,old=queue.popleft()
            image[sr][sc]=color
            dir=[(-1,0),(0,-1),(1,0),(0,1)]
            for row,col in dir:
                nr=sr+row
                nc=sc+col
                if 0 <= nr < len(image) and 0 <= nc < len(image[0]) and image[nr][nc]==old:
                    queue.append((nr,nc,old))
                    image[nr][nc]=color
        return image


        