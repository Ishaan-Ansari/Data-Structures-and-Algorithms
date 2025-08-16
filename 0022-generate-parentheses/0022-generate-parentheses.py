class Solution:
    def solve(self, ans, temp, balance, open_used, n):
        # base contd.
        if len(temp) == 2*n:
            if balance == 0:
                ans.append(temp)
            return 
        
        if open_used < n:
            self.solve(ans, temp+'(', balance+1, open_used+1, n)

        if balance > 0:
            self.solve(ans, temp+')', balance-1, open_used, n)

    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        temp = ""
        balance, open_used = 0, 0
        self.solve(ans, temp, balance, open_used, n)
        return ans
        