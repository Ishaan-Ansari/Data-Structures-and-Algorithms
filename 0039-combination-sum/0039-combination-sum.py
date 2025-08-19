class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        temp = []

        def solve(idx, curr, temp):
            if curr == target:
                ans.append(temp[:])
                return 

            if idx == len(candidates) or curr > target:
                return 

            # add and inc index
            solve(idx, curr+candidates[idx], temp + [candidates[idx]])

            # skip
            solve(idx+1, curr, temp)

        solve(0, 0, [])
        return ans