class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        seen = set(arr)
        missing_count = 0
        num = 1

        while True:
            if num not in seen:
                missing_count +=1
                if missing_count == k:
                    return num
            num +=1

        return -1
