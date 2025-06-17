from typing import List

class Solution:
    def is_possible(self, nums:List[int], m:int, threshPages:int)->bool:
        current_load = 0
        student_used = 1
        for page in nums:
            if page > threshPages:
                return False
                
            if current_load+page<=threshPages:
                current_load+=page
            else:
                current_load = page # start the next student with this book not 0
                student_used +=1
        
        return student_used <= m
                
    
    def findPages(self, nums:List[int], m:int)->int:
        if len(nums)<m:
            return -1
            
        low, high = max(nums), sum(nums)
        ans = -1
        while(low<=high):
            mid = low+(high-low)//2
            if self.is_possible(nums, m, mid):
                ans = mid
                high = mid-1 # it can be further reduced
            else:
                low = mid+1
        
        return ans
    
if __name__ == '__main__':
    nums = [25, 46, 28, 49, 24]
    m=4
    ans = Solution()
    print(ans.findPages(nums, m))
    
