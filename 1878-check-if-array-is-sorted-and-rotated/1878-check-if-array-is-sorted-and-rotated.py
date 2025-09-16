class Solution:
    def check(self, nums: List[int]) -> bool:
        count_num_of_rotations = 0
        n = len(nums)
        for i in range(1, n+1):
            if nums[i-1] > nums[i % n]:
                count_num_of_rotations += 1

        return count_num_of_rotations <= 1