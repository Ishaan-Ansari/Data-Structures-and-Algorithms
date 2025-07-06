class Solution:
    def cal_beauty(self, temp:str) -> int:
        freq = {}
        for ch in temp:
            if ch not in freq:
                freq[ch] = 1
            else:
                freq[ch] += 1
        
        if not freq or len(freq) == 1:
            return 0

        counts = freq.values()
        # values = sorted(freq.items(), lamda x:x[1], reversed=True)
        # return values[0][1]-value[-1][1]

        maxi_diff = max(counts)-min(counts)
        return maxi_diff

    def beautySum(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            temp = ""
            for j in range(i, len(s)):
                temp += s[j]
                if self.cal_beauty(temp) != 0:
                    ans += self.cal_beauty(temp)

        return ans
