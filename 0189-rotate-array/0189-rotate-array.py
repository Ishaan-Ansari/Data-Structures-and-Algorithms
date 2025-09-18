class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp_1 = nums[0:len(nums)-k%len(nums)]
        temp_2 = nums[len(nums)-k%len(nums):]

        nums.clear()
        nums.extend(temp_2)
        nums.extend(temp_1)

        # def rotate_once():
        #     last_elem = nums[-1]
        #     for i in range(len(nums)-1, 0, -1):
        #         nums[i] = nums[i-1]

        #     nums[0] = last_elem

        # for _ in range(k):
        #     rotate_once()
        

        