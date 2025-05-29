class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        max_so_far = nums[0]
        prefix = suffix = 1

        for i in range(0, N):
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1

            prefix *= nums[i]
            suffix *= nums[N-i-1]

            max_so_far = max(max_so_far, max(prefix, suffix))

        return max_so_far

        # maxi = nums[0]

        # for i in range(N):
        #     pdt = 1
        #     for j in range(i, N):
        #         pdt *= nums[j]
        #         maxi = max(maxi, pdt)

        # return maxi
        