from collections import defaultdict

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ans = []
        SUM = 0
        ROW = len(grid)
        COL = len(grid[0])
        freq = defaultdict(int)
        N = ROW*COL

        TOTAL_SUM = (N*(N+1))//2

        for i in range(ROW):
            for j in range(COL):
                freq[grid[i][j]] +=1
                if freq[grid[i][j]] > 1:
                    ans.append(grid[i][j])
    
        for key, value in freq.items():
            SUM += key

        MISSING_NUM = TOTAL_SUM-SUM
        ans.append(MISSING_NUM)
        
        return ans
