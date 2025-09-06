class Solution:
    def cnt_binary_ones(self, n) -> int:
        cnt = 0
        while n > 0:
            if n % 2 == 1:
                cnt += 1
            n = n // 2
        return cnt

    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(0, n+1):
            cnt = self.cnt_binary_ones(i)
            ans.append(cnt)
        
        return ans
