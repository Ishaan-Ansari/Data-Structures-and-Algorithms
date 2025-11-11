class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        left, right = 0, n-k

        if n == k:
            return sum(cardPoints)

        window_sum = sum(cardPoints[right:])
        res = window_sum

        while right < n:
            window_sum += cardPoints[left] - cardPoints[right]
            res = max(res, window_sum)
            left += 1
            right += 1

        return res

        