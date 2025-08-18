MOD = 10**9 + 7

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        if n == 0:
            return 0
        
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = (pow2[i-1] * 2) % MOD
        
        def bin_search(l, r, x):
            res = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] <= x:
                    res = mid
                    l = mid + 1
                else:
                    r = mid - 1
            return res
        
        total = 0
        for i in range(n):
            x = target - nums[i]
            if x < 0:
                continue
            j = bin_search(i, n - 1, x)
            if j >= i:
                total = (total + pow2[j - i]) % MOD
        
        return total