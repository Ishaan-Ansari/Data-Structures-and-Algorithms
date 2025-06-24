class Solution:
    def _get_mini(self, nums, i):
        mini_idx = i
        for idx in range(i+1, len(nums)):
            if nums[idx]<nums[mini_idx]:
                mini_idx = idx
        return mini_idx
        
    def _sel_sort(self, nums):
        for i in range(len(nums)):
            mini_idx = self._get_mini(nums, i)
            nums[i], nums[mini_idx] = nums[mini_idx], nums[i]
            
        return nums
    
    def findMedian(self, matrix):
        row = []
        for idx in matrix:
            row.extend(idx)
        # nums = sorted(row)
        nums = self._sel_sort(row)
        if len(row)%2 != 0:
            return nums[len(nums)//2]
        else:
            mid1 = nums[len(nums)//2]
            mid2 = nums[(len(nums)//2)-1]
            ans = (mid1+mid2)/2
            return ans
        return -1
    
if __name__ == '__main__':
    matrix=[ [1, 4, 9], [2, 5, 6] , [3, 7, 8]]
    ans = Solution()
    print(ans.findMedian(matrix))
