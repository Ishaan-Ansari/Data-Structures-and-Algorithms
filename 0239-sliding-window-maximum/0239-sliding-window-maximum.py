from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k==0:
            return []

        n = len(nums)

        if k == 1:
            return nums[:]

        ans = []
        dq = deque()

        for i in range(n):
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            if i >= k-1:
                ans.append(nums[dq[0]])

        return ans

        # for i in range(n-k+1):
        #     maxi = INT_MIN
        #     for j in range(i, i+k):
        #         maxi = max(maxi, nums[j])
        #     ans.append(maxi)

        # return ans
