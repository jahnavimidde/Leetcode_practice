class Solution:
    def minCost(self, m: int, n: int, penalty: List[List[int]]) -> int:

        def actions(i, j, p):
            # (0,0) -> wait
            # (0,1) -> right
            # (1,0) -> down
            # (0,-1) -> left
            # (-1,0) -> up
            for di, dj in ((0, 0), (0, 1), (1, 0), (0, -1), (-1, 0)):
                ni = i + di
                nj = j + dj

                if 0 <= ni < m and 0 <= nj < n:

                    # Cost of entering the next cell
                    move_cost = 0 if (di == 0 and dj == 0) else (ni + 1) * (nj + 1)

                    # If move direction does not match required parity,
                    # pay the waiting penalty.
                    extra = 0 if (di + dj == p) else penalty[i][j]

                    yield move_cost + extra, (ni, nj, -p)

        # (current_cost, (row, col, parity))
        pq = [(1, (0, 0, 1))]
        seen = set()

        while pq:
            cost, state = heappop(pq)

            if state in seen:
                continue

            seen.add(state)

            i, j, p = state

            if i == m - 1 and j == n - 1:
                return cost

            for add_cost, next_state in actions(i, j, p):
                if next_state not in seen:
                    heappush(pq, (cost + add_cost, next_state))