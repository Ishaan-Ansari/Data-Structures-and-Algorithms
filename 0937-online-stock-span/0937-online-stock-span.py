class StockSpanner:
    def __init__(self):
        self.check = []
        
    def next(self, price: int) -> int:
        num_of_days = 1 # each day counts at least once

        while self.check and self.check[-1][0] <= price:
            num_of_days += self.check.pop()[1]
        
        self.check.append((price, num_of_days))

        return num_of_days

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)