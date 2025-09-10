class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        x = start ^ goal
        cnt = 0

        while x:
            x &= x-1
            cnt += 1

        return cnt
        