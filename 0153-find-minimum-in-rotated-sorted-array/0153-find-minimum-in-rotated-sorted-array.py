class Solution:
    def findMin(self, nums: List[int]) -> int:
        N = len(nums)
        left, right = 0, N-1

        while left<right:
            mid = left+(right-left)//2

            if nums[mid]<=nums[right]:
                right = mid
            else:
                left = mid+1

        return nums[left]
        