class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:  # O(Log(m*n))
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = n-1

        while(i<m and j>=0):
            pos = matrix[i][j]
            if pos == target:
                return True
            if pos>target:
                j -= 1
            elif pos<target:
                i += 1
        return False

    # def binSearch(self, row:List[int], target:int)->bool:       # O(R*Log(C))
    #     low, high = 0, len(row)-1

    #     while low <= high:
    #         mid = low+(high-low)//2
    #         if row[mid] == target:
    #             return True

    #         if row[mid] < target:
    #             low = mid+1
    #         else:
    #             high = mid-1
        
    #     return False

    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     for idx in matrix:
    #         row = idx
    #         if self.binSearch(row, target):
    #             return True
    #     return False
        