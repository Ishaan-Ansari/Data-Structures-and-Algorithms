class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = n-1

        while(i<m and j>=0):
            num = matrix[i][j]
            if num == target:
                return True
            if num > target:
                j -=1
            else:
                i +=1
        
        return False
