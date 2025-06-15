class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        ## O(Log(N))
        low, high = 0, len(arr)-1

        while(low <= high):
            mid = (low+high)//2
            missing = arr[mid]-(mid+1)
            if missing<k:
                low = mid+1
            else:
                high = mid-1

        return k+high+1


        ### O(N)
        # ans = k
        # for num in arr:
        #     if num <= ans:
        #         ans +=1

        #     else:
        #         return ans

        # return ans
