class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [""] * numRows
        currentRow = 0
        goingDown = False
        
        for char in s:
            rows[currentRow] += char
            
            if currentRow == 0 or currentRow == numRows - 1:
                goingDown = not goingDown
                
            currentRow += 1 if goingDown else -1
        
        return "".join(rows)