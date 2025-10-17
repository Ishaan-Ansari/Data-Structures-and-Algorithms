class Solution:
    def prevSmallerElement(self, heights, n):
        stack = []
        prev = [-1]*n

        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            prev[i] = stack[-1] if stack else -1
            stack.append(i)
        return prev
               
    def nextSmallerElement(self, heights, n):
        stack = []
        nxt = [-1]*n

        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            nxt[i] = stack[-1] if stack else -1
            stack.append(i)
        return nxt
        
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0

        n = len(heights)

        prev_smaller = self.prevSmallerElement(heights, n)
        next_smaller = self.nextSmallerElement(heights, n)
        
        max_area = 0
        for i in range(n):
            left = prev_smaller[i]
            right = next_smaller[i] if next_smaller[i] != -1 else n

            width = right - left - 1
            max_area = max(max_area, heights[i] * width)

        return max_area
