class MyQueue:

    def __init__(self):
        self.nums = []

    def push(self, x: int) -> None:
        self.nums.append(x)   

    def pop(self) -> int:
        if not self.nums:
            return 0

        removed_ele = self.nums[0]
        self.nums.pop(0)
        return removed_ele                

    def peek(self) -> int:
        if not self.nums:
            return 0
        return self.nums[0]

    def empty(self) -> bool:
        return len(self.nums) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()