class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        nums = (2**(n-1))
        if k > nums:
            raise ValueError("k out of bounds")
        
        mid = nums//2
        if k <= mid:
            return self.kthGrammar(n-1, k)
        else:
            return 1 - self.kthGrammar(n-1, k-mid)        
