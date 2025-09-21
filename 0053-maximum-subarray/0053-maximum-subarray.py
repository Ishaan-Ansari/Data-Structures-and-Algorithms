class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ending = max_so_far = nums[0]

        for x in nums[1:]:
            max_ending = max(x, max_ending+x)
            max_so_far = max(max_so_far, max_ending)

        return max_so_far

        # for i in range(len(nums)):
        #     temp = 0
        #     for j in range(i, len(nums)):
        #         temp += nums[j]
        #         if temp > ans:
        #             ans = temp

        # return ans