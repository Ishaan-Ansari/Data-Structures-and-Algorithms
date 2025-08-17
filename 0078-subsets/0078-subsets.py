class Solution:
    def solve(self, nums, idx, temp, ans):
        if idx == len(nums):
            ans.append(temp)
            return
        
        # include the number
        self.solve(nums, idx+1, temp+[nums[idx]], ans)

        # exclude the number
        self.solve(nums, idx+1, temp, ans)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        temp = []
        idx = 0

        self.solve(nums, idx, temp, ans)

        return ans