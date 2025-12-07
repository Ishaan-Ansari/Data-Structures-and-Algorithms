import bisect

class MedianFinder:

    def __init__(self):
        self.check = []
        
    def addNum(self, num: int) -> None:
        bisect.insort(self.check, num)      

    def findMedian(self) -> float:
        n = len(self.check)
        ans = 0.0

        if n % 2 == 0:
            ans = (self.check[n//2 - 1] + self.check[n//2])/2.0
        else:
            ans = self.check[n//2]        

        return ans        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()