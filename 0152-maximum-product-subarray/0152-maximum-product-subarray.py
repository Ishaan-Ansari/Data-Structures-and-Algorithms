class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = curr_min = max_so_far = nums[0]

        for num in nums[1:]:
            prev_max, prev_min = curr_max, curr_min

            curr_max = max(num, prev_max*num, prev_min*num)
            curr_min = min(num, prev_max*num, prev_min*num)
            max_so_far = max(max_so_far, curr_max)

        return max_so_far

        # maxi = nums[0]

        # for i in range(N):
        #     pdt = 1
        #     for j in range(i, N):
        #         pdt *= nums[j]
        #         maxi = max(maxi, pdt)

        # return maxi
        