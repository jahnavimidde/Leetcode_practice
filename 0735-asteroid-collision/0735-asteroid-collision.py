class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """

        stack = []

        for num in asteroids:

            if not stack or not (stack[-1] > 0 and num < 0):
                stack.append(num)

            elif abs(stack[-1]) == abs(num):
                stack.pop()

            elif abs(stack[-1]) > abs(num):
                continue

            else:
                destroyed = False

                while stack and stack[-1] > 0:

                    if abs(stack[-1]) < abs(num):
                        stack.pop()

                    elif abs(stack[-1]) == abs(num):
                        stack.pop()
                        destroyed = True
                        break

                    else:
                        destroyed = True
                        break

                if not destroyed and (not stack or stack[-1] < 0):
                    stack.append(num)

        return stack