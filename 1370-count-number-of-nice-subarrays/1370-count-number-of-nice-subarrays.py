class Solution:
    def _helper(self, nums:List[int], k:int)->int:
        if k<0:
            return 0

        count_subarr, start, count_odds = 0, 0, 0

        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                count_odds += 1
            
            while start <= i and count_odds > k:
                if nums[start] % 2 != 0:
                    count_odds -= 1
                start += 1

            count_subarr += (i - start + 1)

        return count_subarr


    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        return self._helper(nums, k) - self._helper(nums, k-1)
        