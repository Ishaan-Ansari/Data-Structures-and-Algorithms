class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        ans = []
        i = 0
        n = len(intervals)
        lo, hi = newInterval

        # add all the intervals ending before the interval
        while i < n and intervals[i][1] < lo:
            ans.append(intervals[i])
            i += 1

        # merge all the overlapping intervals
        while i < n and intervals[i][0] <= hi:
            lo = min(lo, intervals[i][0])
            hi = max(hi, intervals[i][1])
            i += 1

        ans.append([lo, hi])

        # add the remaining intervals
        while i < n:
            ans.append(intervals[i])
            i += 1

        return ans
        