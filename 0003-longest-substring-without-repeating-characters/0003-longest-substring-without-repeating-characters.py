class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l, res = 0, 0
        
        for i in range(len(s)):
            # remove from left until current char is not in the set
            while s[i] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[i])
            res = max(res, i-l+1)

        return res
        