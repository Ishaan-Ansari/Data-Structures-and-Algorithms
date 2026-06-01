class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        less_than_count = 0
        target_count = 0

        for num in nums:
            if num < target:
                less_than_count += 1
            
            elif num == target:
                target_count += 1

        return [i for i in range(less_than_count, less_than_count+target_count)]
        