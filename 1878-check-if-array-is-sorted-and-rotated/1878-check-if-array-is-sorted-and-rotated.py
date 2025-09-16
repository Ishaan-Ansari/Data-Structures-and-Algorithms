class Solution:
    def check(self, nums: List[int]) -> bool:
        count_num_of_rotations = 0
        n = len(nums)

        for i in range(0, n):
            # make sure that the last element of the array is less than or equal to the first element.
            if nums[i] > nums[(i+1) % n]:
                count_num_of_rotations += 1

        return count_num_of_rotations <= 1