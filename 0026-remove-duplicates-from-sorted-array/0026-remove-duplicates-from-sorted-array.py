class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 0

        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                nums[write] = nums[i-1]
                write += 1
        
        nums[write] = nums[len(nums)-1]

        return write+1
