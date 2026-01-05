class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        final_dest = n-1
        max_reach = 0

        for i in range(n):
            if i > max_reach:
                return False

            jump_val = nums[i]
            max_reach = max(max_reach, i+jump_val)

            if max_reach >= final_dest:
                return True


        return False

