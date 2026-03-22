class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        windowStart = 0
        windowSum = 0
        result = float('inf')
        n = len(nums)

        for windowEnd in range(n):
            windowSum += nums[windowEnd]

            while windowSum >= target:
                current_window_size = windowEnd - windowStart + 1
                result = min(result, current_window_size)
                windowSum -= nums[windowStart]
                windowStart += 1

        return 0 if result==float('inf') else result
                
