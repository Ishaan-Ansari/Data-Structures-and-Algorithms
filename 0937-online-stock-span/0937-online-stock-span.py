class StockSpanner:
    def __init__(self):
        self.check = []

    def next(self, price: int) -> int:
        num_of_days = 1 # to count the current span

        while self.check and self.check[-1][0]<=price:
            num_of_days += self.check.pop()[1]

        self.check.append((price, num_of_days))
        return num_of_days
        
        # if self.check:
        #     for i in range(len(self.check)-1, -1, -1):
        #         if price >= self.check[i]:
        #             num_of_days += 1
        #         else:
        #             break
        
        # return num_of_days
        

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)