class Solution:
    def solve(self, nums: List[int], low:int, high:int) -> int:
        if low == high:
            return low

        mid = low + (high-low)//2
        
        # Uphill
        if nums[mid] < nums[mid+1]:
            return self.solve(nums, mid+1, high)

        else: # downhill
            return self.solve(nums, low, mid)

    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        return self.solve(nums, left, right)
        