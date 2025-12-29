class Solution(object):
    def flipAndInvertImage(self, image):
        for row in image:
            left, right = 0, len(row) - 1

            while left <= right:
                # invert and swap
                row[left], row[right] = 1 - row[right], 1 - row[left]
                left += 1
                right -= 1

        return image
