from collections import deque

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        queue = deque()

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (
                    i == 0 or i == len(board)-1 or
                    j == 0 or j == len(board[0])-1
                ):
                    board[i][j] = 'T'      # Mark immediately
                    queue.append((i, j))

        dir = [(-1,0), (0,-1), (1,0), (0,1)]

        while queue:
            row, col = queue.popleft()

            for r, c in dir:
                nr = row + r
                nc = col + c

                if (0 <= nr < len(board) and
                    0 <= nc < len(board[0]) and
                    board[nr][nc] == 'O'):

                    board[nr][nc] = 'T'    # Mark before pushing
                    queue.append((nr, nc))

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'