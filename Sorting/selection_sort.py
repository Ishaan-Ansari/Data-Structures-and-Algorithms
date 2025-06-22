from typing import List

class Sorting:
    def _get_min(self, nums:List[int], index:int)->int:
        """check for min"""
        minIdx = index
        for j in range(index+1, len(nums)):
            if nums[minIdx] > nums[j]:
                minIdx = j
        
        return minIdx

    def selection_sort(self, nums:List[int])->List[int]:      
        """Get the min & place it at first pos"""
        for i in range(0, len(nums)):
            minIdx = self._get_min(nums, i)
            nums[i], nums[minIdx] = nums[minIdx], nums[i]
        return nums
        
if __name__ == '__main__':
    nums = [7, 4, 1, 5, 3]
    srt = Sorting()
    print(srt.selection_sort(nums))    # O(N^2)
