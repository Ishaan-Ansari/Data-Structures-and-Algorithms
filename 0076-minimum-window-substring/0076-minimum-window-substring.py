from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        INT_MAX = 10**8 - 1

        if len(t) > n:
            return ""


        ft = defaultdict(int)
        for ch in t:
            ft[ch] += 1

        mpp = defaultdict(int, ft)

        requiredCount = len(t)
        i, j = 0, 0

        minWindowsize = INT_MAX
        start_i = 0

        while j < n:
            ch = s[j]

            if mpp[ch] and mpp[ch]>0:
                requiredCount -= 1
            
            mpp[ch] -= 1

            while requiredCount == 0:

                currWindowsize = j-i+1


                if minWindowsize > currWindowsize:
                    minWindowsize = currWindowsize
                    start_i = i

                startChar = s[i]
                mpp[startChar] += 1

                if mpp[startChar] and mpp[startChar]>0:
                    requiredCount += 1

                i += 1
            j += 1
        
        if minWindowsize == INT_MAX:
            return ""
        return s[start_i: start_i + minWindowsize]
