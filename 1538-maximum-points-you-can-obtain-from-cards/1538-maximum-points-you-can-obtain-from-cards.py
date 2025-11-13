class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)

        if n==k:
            return sum(cardPoints)

        left_sum = sum(cardPoints[:k])        
        right_sum = 0

        left, right = k-1, n-1
        maxi = left_sum

        while left >= 0:
            window_sum = left_sum + right_sum
            maxi = max(maxi, window_sum)

            left_sum -= cardPoints[left]
            right_sum += cardPoints[right]
            left -= 1
            right -= 1

        maxi = max(maxi, right_sum)
            
        return maxi

        # n = len(cardPoints)
        # left, right = 0, n-k

        # if n == k:
        #     return sum(cardPoints)

        # window_sum = sum(cardPoints[right:])
        # res = window_sum

        # while right < n:
        #     window_sum += cardPoints[left] - cardPoints[right]
        #     res = max(res, window_sum)
        #     left += 1
        #     right += 1

        # return res
        