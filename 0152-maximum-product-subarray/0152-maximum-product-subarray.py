class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best = worst = ans = nums[0]

        for num in nums[1:]:
            if num < 0:
                best, worst = worst, best
            
            best = max(num, best*num)
            worst = min(num, worst*num)
            ans = max(ans, best)

        return ans