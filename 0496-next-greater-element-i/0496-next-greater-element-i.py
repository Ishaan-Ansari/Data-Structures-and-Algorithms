class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                index = nums2.index(nums1[i])
                for j in range(index, len(nums2)):
                    if nums2[j] > nums2[index]:
                        ans.append(nums2[j])
                        break
                else:
                    ans.append(-1)

        return ans                
