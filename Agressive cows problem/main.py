class Solution:
    def is_possible(self, nums, gap, k) -> bool:
        cnt = 1
        last_pos = nums[0]
        for each_stall in nums[1:]:
            if each_stall-last_pos>=gap:
                cnt +=1
                last_pos = each_stall
                if cnt == k:
                    return True
                    
        return False   

    def aggressiveCows(self, nums, k):
        nums = sorted(nums)
        low, high = 1, max(nums)-min(nums)
        ans = None

        while low<=high:
            mid = (low+high)//2
            if self.is_possible(nums, mid, k):
                ans = mid
                low = mid+1

            else:
                high = mid-1

        return ans
        
ans = Solution()

k = 2
nums = [4, 2, 1, 3, 6]

solve = ans.aggressiveCows(nums, k)
print(solve)
