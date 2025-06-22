class Solution:
    # Apply only when mat is sorted row wise
    def rowWithMax1sBest(self, mat):    # O(M+N)
        m = len(mat)
        n = len(mat[0])
        
        i = 0
        j = n-1
        
        ans_row = -1
        
        while i<m and j>=0:
            if mat[i][j] == 1:
                ans_row = i
                j -= 1
            else:
                i += 1

        return ans_row

    def countOnes(self, row):
        cnt = 0
        for num in row:
            if num == 1:
                cnt +=1
        return cnt

    def rowWithMax1sBetter(self, mat):
        ans_row = 0
        max_count = 0
        
        for idx, row in enumerate(mat):
            count = self.countOnes(row)
            if count > max_count:
                ans_row = idx
                max_count = count
        
        return ans_row
        
    def rowWithMax1s(self, mat):
        check = {}
        for idx, row in enumerate(mat):
            check[idx] = self.countOnes(row)

        sorted_items = sorted(check.items(), key=lambda item:item[1], reverse=True)
        
        if sorted_items[0][0] == 0:
            return -1
            
        return sorted_items[0][0]
        
        
if __name__ == '__main__':
    mat = [ [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    # mat =  [ [0, 0], [0, 0] ]
    ans = Solution()
    print(ans.rowWithMax1sBest(mat))
