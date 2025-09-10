class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        x = start ^ goal
        cnt = 0

        while x:
            rsbm = x & -x
            x = x - rsbm
            cnt += 1

        return cnt
        