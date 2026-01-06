class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        index = n-1

        for i in range(n-1, -1, -1):
            if nums[i]+i >= index:
                index = i

        return index == 0