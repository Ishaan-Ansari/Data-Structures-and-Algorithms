class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = []
        
        for i in range(len(nums)):
            flag = False
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    ans.append(nums[j])
                    flag = True
                    break

            if flag is not True:
                for k in range(0, i):
                    if nums[k] > nums[i]:
                        ans.append(nums[k])
                        break
                else:
                    ans.append(-1)

        return ans
