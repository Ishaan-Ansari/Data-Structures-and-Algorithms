class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        check={}
        for i, num in enumerate(nums):
            complement=target-nums[i]
            if complement in check:
                return [check[complement], i]
            check[nums[i]]=i
        return []
            
