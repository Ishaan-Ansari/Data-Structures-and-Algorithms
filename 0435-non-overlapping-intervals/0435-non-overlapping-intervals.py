class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda kv:kv[1])

        n = len(intervals)
        lo, hi = intervals[0]
        
        ans = []
        ans.append(intervals[0])
        
        i = 1
        while i<n:
            if intervals[i][0] >= hi:
                ans.append(intervals[i])
                hi = intervals[i][1]
            i += 1

        return len(intervals) - len(ans)
