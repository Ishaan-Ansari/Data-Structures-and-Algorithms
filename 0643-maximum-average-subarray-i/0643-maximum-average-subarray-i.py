class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        results = []
        windowSum = 0
        windowStart = 0

        for i in range(len(nums)):
            windowSum += nums[i]

            if i >= k-1:
                results.append(windowSum/k)
                windowSum -= nums[windowStart]

                windowStart +=1 

        return max(results)
