from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        if not nums:
            return 0

        n = len(nums)

        mpp = defaultdict(int)
        mpp[0] = 1
        preSum = 0
        counts = 0

        for i in range(n):
            preSum += nums[i]
            need = preSum - goal
            found = mpp[need]
            counts += found
            mpp[preSum] += 1
                        
        return counts
        