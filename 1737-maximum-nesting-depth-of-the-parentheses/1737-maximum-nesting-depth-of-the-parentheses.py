class Solution:
    def maxDepth(self, s: str) -> int:
        maxDepth = 0
        cnt_out = cnt_in = 0
        
        for i in range(len(s)):
            if s[i] == "(":
                cnt_out += 1
            elif s[i] == ")":
                cnt_in += 1
            
            diff = cnt_out-cnt_in

            if diff>maxDepth:
                maxDepth = diff

        return maxDepth