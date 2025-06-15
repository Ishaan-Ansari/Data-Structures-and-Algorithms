class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        ans = k
        for num in arr:
            if num <= ans:
                ans +=1

            else:
                return ans

        return ans
