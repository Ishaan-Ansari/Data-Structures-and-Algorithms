class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        check = start ^ goal
        check = bin(check)
        check_without_prefix = check.replace("0b", "")

        cnt = 0
        for i in range(len(check_without_prefix)):
            if check_without_prefix[i] == "1":
                cnt += 1

        return cnt
