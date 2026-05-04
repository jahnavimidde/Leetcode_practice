class Solution(object):
    def findRotation(self, mat, target):
        n = len(mat)

        for _ in range(4):   # check 0°, 90°, 180°, 270°
            if mat == target:
                return True

            # transpose
            for i in range(n):
                for j in range(i + 1, n):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

            # reverse columns (row-wise)
            low = 0
            high = n - 1
            while low < high:
                for i in range(n):
                    mat[i][low], mat[i][high] = mat[i][high], mat[i][low]
                low += 1
                high -= 1

        return False
