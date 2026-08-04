class Solution(object):
    def bs(self, prefix, target):
        l, r = 0, len(prefix) - 1
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            if prefix[mid] <= target:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans

    def countTasks(self, tasks, shifts):
        

        n = len(tasks)

        prefix = [0] * n
        prefix[0] = tasks[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + tasks[i]

        total = prefix[-1]

        ans = []

        j = 0
        remained = tasks[0]

        for shift in shifts:

            if j == 0 and remained == tasks[0]:

                if shift >= total:
                    ans.append(0)
                    continue

                idx = self.bs(prefix, shift)

                

                j = idx + 1
                prev = prefix[idx] if idx != -1 else 0
                remained = tasks[j] - (shift - prev)
                ans.append(n - j)
                continue

            while True:

                if shift < remained:
                    remained -= shift
                    ans.append(n - j)
                    break

                shift -= remained
                j += 1

                if j == n:
                    ans.append(0)
                    j = 0
                    remained = tasks[0]
                    break

                remained = tasks[j]

        return ans