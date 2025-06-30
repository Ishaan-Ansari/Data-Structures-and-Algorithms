class Solution:
    def frequencySort(self, s: str) -> str:
        ans = ""
        freq = {}

        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
        
        for key, values in sorted(freq.items(), key=lambda x:x[1], reverse=True):
            for i in range(values):
                ans += key

        return ans
