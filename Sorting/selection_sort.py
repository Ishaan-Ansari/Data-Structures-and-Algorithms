from typing import List

class Sorting:
  def __init__(self, nums: List[int]):
    self.nums = nums
    
  def _selection_sort(self):
    N = len(self.nums)
    for i in range(N):
      min_idx = i
      for j in range(i, N):
        if self.nums[j] < self.nums[min_idx]:
          min_idx = j

      self.nums[min_idx], self.nums[i] = self.nums[i], self.nums[min_idx]

    return self.nums

  def _bubble_sort(self):
    N = len(self.nums)
    for i in range(N):
      swapped = False
      for j in range(1, N):
        if self.nums[j-1] > self.nums[j]:
          self.nums[j-1], self.nums[j] = self.nums[j], self.nums[j-1]
          swapped = True

      # if we went through the whole array and no elements swapped, It's sorted.
      if not swapped:
        break

    return self.nums 

  def _insertion_sort(self):
    N = len(self.nums)
    # considering first element as sorted
    i = 1
    while i<N:
      for j in range(i, 0, -1):
        if self.nums[j-1] > self.nums[j]:
          self.nums[j-1], self.nums[j] = self.nums[j], self.nums[j-1]
        else:
          break

      i += 1

    return self.nums
    


if __name__ == '__main__':
    nums = [7, 4, 1, 5, 3]
    srt = Sorting(nums)
    # print(srt._selection_sort())
    print(srt._insertion_sort())  
