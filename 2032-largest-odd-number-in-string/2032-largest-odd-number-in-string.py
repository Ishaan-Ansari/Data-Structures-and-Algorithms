class Solution:
    def largestOddNumber(self, num: str) -> str:
        idx = len(num)-1
        temp = ""
        
        while(idx >= 0):
            check_num = int(num[idx])
            if check_num % 2 == 0:
                idx -= 1
            else:
                break

        for i in range(0, idx+1):
            temp += num[i]

        return temp


