class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        left, right = 0, n-1
        
        while left <= right:
            mid = left+(right-left)//2
            max_row = max(range(m), key=lambda i: mat[i][mid])
            mid_val = mat[max_row][mid]

            left_val = mat[max_row][mid-1] if mid-1>=0 else float('-inf')
            right_val = mat[max_row][mid+1] if mid+1<n else float('-inf')

            if mid_val>left_val and mid_val>right_val:
                return [max_row, mid]

            if left_val > mid_val:
                right = mid-1
            else:
                left = mid+1
        
        return [-1, -1]



        