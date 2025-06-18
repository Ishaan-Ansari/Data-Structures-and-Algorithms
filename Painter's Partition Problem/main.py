from typing import List

class Solution:
    def is_possible(self, boards:int, k:int, maxTime:int)->bool:
        # Check if it's possible to paint all boards within max_time
        time_cnt = 0
        painters_used = 1
        for time in boards:
            if time > maxTime:
                return False
                
            if time_cnt+time<=maxTime:
                time_cnt += time
            else:
                time_cnt = time
                painters_used += 1
            
        return painters_used<=k
    
    def PainterPartionProlem(self, boards:List[int], k:int)->int:
        low, high = max(boards), sum(boards)
        
        while(low<=high):
            mid = low+(high-low)//2
            if self.is_possible(boards, k, mid):
                ans = mid
                high = mid-1
            else:
                low = mid+1
                
        return ans
    
if __name__ == "__main__":
    # boards = [5, 5, 5, 5]
    # k = 2   # Painters
    
    boards = [10, 20, 30, 40]
    k = 2

    ans = Solution()
    print(ans.PainterPartionProlem(boards, k))
    
