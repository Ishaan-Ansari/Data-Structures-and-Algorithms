class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        left, right = 0, N-1

        while left<=right:
            mid = left-(left-right)//2
            if nums[mid] == target:
                return mid

            # condition for left half being sorted
            if nums[left] < nums[mid]:
                if nums[left] < target and target<nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if nums[mid]>target and target>nums[right]:
                    left = mid+1
                else:
                    right = mid-1
            
            return -1

        