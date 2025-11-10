class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        if n < 3:
            return 0

        count = [0, 0, 0]
        left, result = 0, 0

        for right, ch in enumerate(s):
            count[ord(ch) - ord('a')] += 1
            
            while count[0] > 0 and count[1] > 0 and count[2] > 0:
                count[ord(s[left]) - ord('a')] -= 1
                left += 1

            result += left

        return result


        # for i in range(n):
        #     temp = ""
        #     for j in range(i, n):
        #         temp += s[j]
        #         if ("a" in temp and "b" in temp and "c" in temp):
        #             count += 1

        return count
