class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        N = len(nums)
        left, right = 0, N-1

        while left<right:
            mid = left+(right-left)//2
            if mid % 2 == 0:
                if nums[mid] == nums[mid+1]:
                    left = mid+1
                else:
                    right = mid

            else:
                if nums[mid] == nums[mid-1]:
                    left = mid+1
                else:
                    right = mid

        return nums[left]

