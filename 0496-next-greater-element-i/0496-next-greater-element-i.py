from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapp = {}
        stack = []
        res = []
        for num in nums2:
            while stack and num > stack[-1]:
                mapp[stack.pop()] = num
            stack.append(num)
        for element in stack:
            mapp[element] = -1
        for i in nums1:
            res.append(mapp[i])
        return res