class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        n = len(intervals)

        if not intervals:
            return []

        intervals.sort(key=lambda kv:kv[0])

        lo =  intervals[0][0]
        hi = intervals[0][1]

        i = 1

        while i < n:
            if intervals[i][0] <= hi:
                hi = max(hi, intervals[i][1])
            else:
                ans.append([lo, hi])
                lo = intervals[i][0]
                hi = intervals[i][1]

            i += 1

        ans.append([lo, hi])

        return ans
        