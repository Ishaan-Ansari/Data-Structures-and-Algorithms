class Solution:
    def remove_leading_zero(self, nums):
        i = 0
        while i<len(nums) and nums[i] == '0':
            i += 1

        if i == len(nums):
            return '0'
        
        return nums[i:]

    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return "0"

        stack = []
        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        if k:
            stack = stack[:-k]

        result = ''.join(stack).lstrip('0')
        return result if result else "0"


        # if k == len(num):
        #     return "0"

        # for i in range(k):
        #     to_remove_index = 0
        #     while to_remove_index<len(num)-1 and num[to_remove_index] <= num[to_remove_index + 1]:
        #         to_remove_index += 1
        
        #     num = num[:to_remove_index] + num[to_remove_index+1:]

        # if not num:
        #     return "0"
            
        # return self.remove_leading_zero(num)