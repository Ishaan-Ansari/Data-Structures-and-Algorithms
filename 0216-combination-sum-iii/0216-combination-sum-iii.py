class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        nums = list(range(1, 10))
        ans = []
        
        def solve(curr, idx, pos, temp):
            if curr == n and pos == k:
                ans.append(temp[:])
                return
            
            if curr > n or pos > k or idx >= len(nums):
                return

            temp.append(nums[idx])
            solve(curr + nums[idx], idx+1, pos+1, temp)
            temp.pop()
            
            solve(curr, idx+1, pos, temp) 

        solve(0, 0, 0, [])
        return ans
