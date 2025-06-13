from math import ceil

class Solution:
    def dev_sum(self, nums: List[int], n: int)->int:
        ans = sum(ceil(num/n) for num in nums)
        return ans

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        lo, hi = 1, max(nums)
        ans = None

        while(lo <= hi):
            mid = (lo+hi)//2

            if self.dev_sum(nums, mid) > threshold:
                lo = mid+1
            else:
                ans = mid
                hi = mid-1

        return ans        
