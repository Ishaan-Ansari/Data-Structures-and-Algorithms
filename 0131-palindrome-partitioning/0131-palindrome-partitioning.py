class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        idx = 0

        def solve(idx, temp_lst):
            if idx == len(s):
                ans.append(temp_lst[:])
                return 

            for end in range(idx, len(s)):
                sub = s[idx:end+1]
                if sub == sub[::-1]:        
                    temp_lst.append(sub)        
                    solve(end + 1, temp_lst)    # recurse
                    temp_lst.pop()              # backtrack

        solve(0, [])
        return ans