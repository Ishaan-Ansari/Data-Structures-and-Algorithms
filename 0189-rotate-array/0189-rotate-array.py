class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0:
            return

        k %= n
        if k == 0:
            return

        def reverse(l:int, r:int):
            while l<r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        # first reverse the whole array
        reverse(0, n-1)

        # then reverse the first k elems
        reverse(0, k-1)

        # reverse the remaining elems
        reverse(k, n-1)

        # -------------------------------------------------

        # temp1 = nums[0:len(nums)-k%len(nums)]
        # temp2 = nums[len(nums)-k%len(nums):]

        # nums.clear()
        # nums.extend(temp2)
        # nums.extend(temp1)

        #---------------------------------------------------
        
        # def rotate_once():
        #     last_elem = nums[-1]
        #     for i in range(len(nums)-1, 0, -1):
        #         nums[i] = nums[i-1]

        #     nums[0] = last_elem

        # for _ in range(k):
        #     rotate_once()
        

        