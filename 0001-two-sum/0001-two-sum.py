class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        check = {}

        for i in range(len(nums)):
            if target-nums[i] in check:
                ans.append(check[target-nums[i]])
                ans.append(i)
            else:
                check[nums[i]] = i
        
        return ans
