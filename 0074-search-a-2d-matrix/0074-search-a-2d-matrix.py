class Solution:
    def binSearch(self, row:List[int], target:int)->bool:
        low, high = 0, len(row)-1

        while low <= high:
            mid = low+(high-low)//2
            if row[mid] == target:
                return True

            if row[mid] < target:
                low = mid+1
            else:
                high = mid-1
        
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for idx in matrix:
            row = idx
            if self.binSearch(row, target):
                return True
        return False
        