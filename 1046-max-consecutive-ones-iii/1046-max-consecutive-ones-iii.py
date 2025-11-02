class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zeros = 0
        maxlen = 0

        for right, val in enumerate(nums):
            if val == 0:
                zeros += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            
            maxlen = max(maxlen, right-left+1)

        return maxlen

        # maxi = 0
        # n = len(nums)

        # for i in range(n):
        #     count_zeros = 0
        #     for j in range(i, n):
        #         if nums[j] == 0:
        #             count_zeros += 1

        #         if count_zeros <= k:
        #             maxi = max(maxi, j-i+1)

        # return maxi
