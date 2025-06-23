class Solution:
    def _get_maxi(self, mat:List[List[int]], m:int, mid:int)->int:
        max_row_idx = -1
        max_val = float('-inf')

        for i in range(0, m):
            if mat[i][mid]>max_val:
                max_val = mat[i][mid]
                max_row_idx = i

        return max_row_idx

    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        low, high = 0, n-1

        while(low<=high):
            mid = low+(high-low)//2    # column

            # get maximum in col
            max_row = self._get_maxi(mat, m, mid)   # row

            left = mat[max_row][mid-1] if mid-1>=0 else -1
            right = mat[max_row][mid+1] if mid+1<n else -1

            if mat[max_row][mid]>left and mat[max_row][mid]>right:
                return [max_row, mid]

            if left > mat[max_row][mid]:
                high = mid-1

            else:
                low = mid+1

        return [-1, -1]


