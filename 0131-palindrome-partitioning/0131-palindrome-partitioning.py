class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def solve(idx, curr, temp):
            if idx == len(s):
                ans.append(temp[:])
                return

            for i in range(idx, len(s)):
                curr = s[idx:i+1]
                if curr == curr[::-1]:
                    temp.append(curr)
                    solve(i+1, curr, temp)    # recurse
                    temp.pop()  # backtrack

        solve(0, "", [])
        return ans