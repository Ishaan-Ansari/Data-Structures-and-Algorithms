class Solution:
    def is_possible(self, nums: List[int], k: int, threshSum:int)->bool:
        curr_sum = 0
        sub_arr_cnt = 1

        for num in nums:
            if num > threshSum:
                return False

            if num+curr_sum<=threshSum:
                curr_sum += num

            else:
                curr_sum = num
                sub_arr_cnt +=1
            
        return sub_arr_cnt <= k

    def splitArray(self, nums: List[int], k: int) -> int:
        if len(nums)<k:
            return -1

        low, high = max(nums), sum(nums)
        ans = -1

        while(low<=high):
            mid = low+(high-low)//2
            if self.is_possible(nums, k, mid):
                ans = mid
                high = mid-1    # It can be further reduced
            else:
                low = mid+1

        return ans
                
