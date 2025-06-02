class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        N = len(nums)
        left, right = 0, N-1

        while left<= right:
            mid = left+(right-left)//2
            if nums[mid] == target:
                return True

            if nums[mid] == nums[left] == nums[right]:
                left +=1
                right -=1
                continue

            if nums[left] <= nums[mid]:
                if nums[left]<=target and target<nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if nums[right]>=target and target>nums[mid]:
                    left = mid+1
                else:
                    right = mid-1
        return False
