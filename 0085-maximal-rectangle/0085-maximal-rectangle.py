class Solution:
    def prevSmaller(self, row: List[int], n: int):
        prev = [-1]*n
        stack = []

        for i in range(n):
            while stack and row[stack[-1]] >= row[i]:
                stack.pop()
            prev[i] = stack[-1] if stack else -1
            stack.append(i)
            
        return prev

    def nextSmaller(self, row: List[int], n: int):
        nxt = [n]*n
        stack = []

        for i in range(n-1, -1, -1):
            while stack and row[stack[-1]] >= row[i]:
                stack.pop()
            nxt[i] = stack[-1] if stack else n
            stack.append(i)
        return nxt
    
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        row = len(matrix)
        col = len(matrix[0])
        temp = [0]*col

        max_area = 0

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == '1' or matrix[i][j] == 1:
                    temp[j] += 1
                else:
                    temp[j] = 0

            # temp = [a+b for a,b in zip(temp, matrix[i])]
            prev_smaller = self.prevSmaller(temp, col)
            nxt_smaller = self.nextSmaller(temp, col)

            for j in range(col):
                width = nxt_smaller[j] - prev_smaller[j] - 1
                area = temp[j]*width
                max_area = max(max_area, area)

        return max_area
