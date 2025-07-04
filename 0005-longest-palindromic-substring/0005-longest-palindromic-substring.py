class Solution:
    def longestPalindrome(self, s: str) -> str:
        mx = 0
        ans = ""
        mx = 0

        for i in range(len(s)):
            temp = ""
            for j in range(i, len(s)):
                temp += s[j]
                if temp == temp[::-1]:
                    if len(temp) > mx:
                        mx = len(temp)
                        ans = temp

        return ans
        