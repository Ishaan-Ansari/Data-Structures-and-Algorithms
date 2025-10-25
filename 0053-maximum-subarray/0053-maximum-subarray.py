class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = max_so_far = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_so_far = max(max_so_far, current_sum)

        return max_so_far
        