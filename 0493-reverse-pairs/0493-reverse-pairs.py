from typing import List

class Solution:
    def __init__(self):
        self.count = 0

    def merge(self, left: List[int], right: List[int]) -> List[int]:
        # 1) count cross-pair inversions
        j = 0
        for i in range(len(left)):
            while j < len(right) and left[i] > 2 * right[j]:
                j += 1
            self.count += j

        # 2) actually merge the two sorted halves
        ans = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                ans.append(left[i])
                i += 1
            else:
                ans.append(right[j])
                j += 1

        # 3) append any leftovers
        ans.extend(left[i:])
        ans.extend(right[j:])
        return ans

    def merge_sort(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left_sorted = self.merge_sort(nums[:mid])
        right_sorted = self.merge_sort(nums[mid:])
        return self.merge(left_sorted, right_sorted)

    def reversePairs(self, nums: List[int]) -> int:
        self.count = 0
        self.merge_sort(nums)
        return self.count
