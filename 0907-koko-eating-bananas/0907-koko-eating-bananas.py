from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)

        while low <= high:
            mid = (low+high)//2
            total_hours = sum(ceil(pile/mid) for pile in piles)
            
            if total_hours <= h:
                high = mid-1
            else:
                low = mid+1

        return low
        