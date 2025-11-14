from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        return self.atmostK(nums, k) - self.atmostK(nums, k-1)
    
    def atmostK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left, res = 0, 0
        mpp = defaultdict(int)

        for right in range(len(nums)):
            val = nums[right]
            mpp[val] += 1

            while len(mpp) > k:
                left_val = nums[left]
                mpp[left_val] -= 1

                if mpp[left_val] == 0:
                    del mpp[left_val]

                left += 1    

            res += (right - left + 1)                   
            
        return res

    
        # n = len(nums)
        # res = 0

        # for i in range(n):
        #     st = set()
        #     for j in range(i, n):
        #         st.add(nums[j])
        #         if len(st) > k:
        #             break
        #         if len(st) == k:
        #             res += 1
   
        # return res
        