# merge sort
def merge_sort(arr):
  if len(arr) <= 1:
    return arr

  # PHASE 1: Divide 
  mid = len(arr)//2
  left_half = arr[:mid]
  right_half = arr[mid:]

  sorted_left = merge_sort(left_half)
  sorted_right = merge_sort(right_half)

  return merge(sorted_left, sorted_right)

def merge(left, right):
  sorted_results = []

  i, j = 0, 0

  while i<len(left) and j<len(right):
    if left[i] < right[j]:
      sorted_results.append(left[i])
      i += 1
    else:
      sorted_results.append(right[j])
      j += 1

  # whatever is left
  sorted_results.extend(left[i:])
  sorted_results.extend(right[j:])

  return sorted_results
      


arr = [10, 9, 4, 5, 1, 3, 2, 7, 6]
print(merge_sort(arr))
