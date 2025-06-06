class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 0:
            return None
        if N == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[N-1] != nums[N-2]:
            return nums[N-1]

        left, right = 1, len(nums)-2

        while(left<=right):
            mid = left + (right-left)//2

            if nums[mid-1] != nums[mid] and nums[mid] != nums[mid+1]:  # single element 
                return nums[mid]

            # we're in the left half
            if (mid%2 == 1 and (nums[mid] == nums[mid-1])) or (mid%2 == 0 and (nums[mid] == nums[mid+1])):
                left = mid+1
            else:
                right = mid-1

        return -1