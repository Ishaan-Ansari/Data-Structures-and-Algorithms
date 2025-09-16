class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        st = set(nums)
        nums.clear()
        
        for num in st:
            nums.append(num)

        nums.sort()
        return len(nums)
