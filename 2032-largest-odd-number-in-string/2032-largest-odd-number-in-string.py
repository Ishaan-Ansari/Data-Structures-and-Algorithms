class Solution:
    def largestOddNumber(self, num: str) -> str:
        idx = len(num)-1
        temp = ""
        
        while (idx >= 0) and (int(num[idx]) % 2 == 0):
            idx -= 1
            # check_num = int(num[idx])
            # if check_num % 2 == 0:
            #     idx -= 1
            # else:
            #     break

        # for i in range(0, idx+1):         # remove manual concat
        #     temp += num[i]

        return num[0:idx+1]     # using string slicing instead

