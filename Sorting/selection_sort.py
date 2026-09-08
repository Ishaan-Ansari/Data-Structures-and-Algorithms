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

  def _quick_sort(self, arr=None):
    if arr is None:
      arr = self.nums

    # At what point is this problem so ridiculously small that the answer is obvious?
    if len(arr) <= 1:
      return arr

    pivot = arr[len(arr)//2]

    less = [x for x in arr if x<pivot]
    equal = [x for x in arr if x==pivot]
    greater = [x for x in arr if x>pivot]

    return self._quick_sort(less) + equal + self._quick_sort(greater)


if __name__ == '__main__':
    nums = [4,6,2,5,7,9,1,3]
    srt = Sorting(nums)
    # print(srt._selection_sort())
    print(srt._quick_sort())    
