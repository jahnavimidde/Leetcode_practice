class Solution:
    def primePalindrome(self, n: int) -> int:

        def is_prime(num):
            if num < 2:
                return False

            if num % 2 == 0:
                return num == 2

            i = 3
            while i * i <= num:
                if num % i == 0:
                    return False
                i += 2

            return True

        
        for p in [2, 3, 5, 7, 11]:
            if n <= p:
                return p

        # all even length prime numbers are divisible by 11 so no need to check even length
        for half in range(10, 100000):    # handled 1 digit now handle 3 digit onwards
            s = str(half)
            palindrome = int(s + s[-2::-1])

            if palindrome >= n and is_prime(palindrome):
                return palindrome