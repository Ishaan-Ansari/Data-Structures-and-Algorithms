class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        gre = {}

        for num in nums2:
            while stack and stack[-1] < num:
                gre[stack.pop()] = num
            stack.append(num)
        for num in stack:
            gre[num] = -1

        return [gre[num] for num in nums1]