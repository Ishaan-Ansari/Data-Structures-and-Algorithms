class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        def solve(idx, temp):
            if idx >= len(nums):
                ans.append(temp[:])
                return 

            # include the number
            temp.append(nums[idx])
            solve(idx+1, temp)
            temp.pop()

            j = idx
            while (j + 1 < len(nums) and nums[j] == nums[j+1]):
                j += 1

            # don't pick                
            solve(j+1, temp)

        solve(0, [])
        return ans