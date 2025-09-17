class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # nums starts with 1 index because first element is always unique
        write = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[write] = nums[i]
                write += 1
    
        return write
