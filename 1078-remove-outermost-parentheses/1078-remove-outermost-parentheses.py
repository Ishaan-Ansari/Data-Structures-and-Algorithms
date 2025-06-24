class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = ""
        depth = 0
        for i in range(len(s)):
            if s[i] == '(':
                if depth>=1:
                    ans += '('
                depth += 1
            elif s[i] == ')':
                depth -= 1
                if depth >= 1:
                    ans += ')'
        return ans

        