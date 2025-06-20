class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = sorted(nums1+nums2)
        total_len = len(nums3)
        mid_index = total_len//2

        if total_len % 2 != 0:
            return nums3[mid_index]
        return (nums3[mid_index]+nums3[mid_index-1])/2.0