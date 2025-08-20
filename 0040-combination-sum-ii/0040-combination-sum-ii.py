class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        temp = []

        def solve(idx, curr, temp):
            if curr == target:
                ans.append(temp[:])
                return
            
            if idx == len(candidates) or curr > target:
                return 
            
            # include, add, increment
            if curr + candidates[idx] <= target:
                solve(idx+1, curr+candidates[idx], temp+[candidates[idx]])

            j = idx + 1
            while j < len(candidates) and candidates[j] == candidates[idx]:
                j += 1

            # exclude 
            solve(j, curr, temp)

        solve(0, 0, [])
        return ans
