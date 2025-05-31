class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        left, right = 0, N-1
        first_idx, last_idx = -1, -1

        while(left<=right):
            mid = left+(right-left)//2
            if nums[mid] < target:
                left = mid+1
            else:
                if nums[mid] == target:
                    first_idx = mid
                right = mid-1

        if first_idx == -1:
            return [-1, -1]

        left, right = 0, N-1

        while(left<=right):
            mid = left+(right-left)//2
            if nums[mid] > target:
                right = mid-1
            else:
                if nums[mid] == target:
                    last_idx = mid
                left = mid+1


        return [first_idx, last_idx]            
        