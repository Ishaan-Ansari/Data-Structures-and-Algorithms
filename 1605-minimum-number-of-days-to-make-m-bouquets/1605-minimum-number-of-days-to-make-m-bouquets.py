class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m*k:
            return -1

        def can_make(day):
            flower, bouquet = 0, 0
            for bday in bloomDay:
                if bday<=day:
                    flower +=1
                    if flower == k:
                        bouquet +=1
                        flower = 0
                        if bouquet == m:
                            return True
                        
                else:
                    flower = 0
            return False

        ans = -1
        minDay = min(bloomDay)
        maxDay = max(bloomDay)

        while(minDay <= maxDay):
            mid = (minDay+maxDay)//2

            if can_make(mid):
                ans=mid
                maxDay = mid-1
            else:
                minDay = mid+1

        return ans