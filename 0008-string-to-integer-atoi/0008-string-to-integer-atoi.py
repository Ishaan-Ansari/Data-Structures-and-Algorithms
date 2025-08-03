class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        neg = False
        start, ans = 0, 0

        if s[0] in ('-', '+'):
            neg = (s[0] == '-')
            start = 1
        
        for i in range(start, len(s)):
            if s[i].isdigit():
                ans = ans*10+int(s[i])
                if neg and ans > 2**31:
                    return -2**31
                elif not neg and ans > 2**31-1:
                    return 2**31-1
            else:
                break

        if neg:
            ans = -ans

        if ans<-2**31:
            return -2**31-1
        elif ans>2**31-1:
            return 2**31-1

        return ans
