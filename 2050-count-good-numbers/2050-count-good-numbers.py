import math 

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        even_count = (n + 1) // 2
        odd_count = (n // 2)

        even_pos = pow(5, even_count, MOD)
        odd_pos = pow(4, odd_count, MOD)

        ans = (even_pos * odd_pos) % MOD
        return ans
        # if n % 2 == 0:
        #     even_pos = 5**(n//2)
        #     odd_pos = 4**(n//2)
        # elif n % 2 != 0:
        #     even_pos = 5**(math.ceil(n/2))
        #     odd_pos = 4**(math.floor(n/2))

        # ans = (even_pos*odd_pos) % INT_MAX
        # return ans

