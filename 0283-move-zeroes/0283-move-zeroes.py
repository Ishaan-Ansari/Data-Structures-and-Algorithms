class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        insertPos = 0

        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[insertPos], nums[i] = nums[i], nums[insertPos]
                insertPos += 1

        # while insertPos < len(nums):
        #     nums[insertPos] = 0
        #     insertPos += 1
        