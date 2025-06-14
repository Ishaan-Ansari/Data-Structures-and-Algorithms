class Solution:
    def is_possible(self, weights: List[int], cap: int)->int:
        days, curr_wt = 1, 0

        for wt in weights:
            if curr_wt+wt > cap:        # check if adding this wt will exceed the cap
                days += 1
                curr_wt = 0
            curr_wt += wt

        return days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        ans = high

        while(low <= high):
            mid = (low+high)//2
            if self.is_possible(weights, mid) > days:
                low = mid+1
            else:
                ans = mid
                high = mid-1
        
        return ans
