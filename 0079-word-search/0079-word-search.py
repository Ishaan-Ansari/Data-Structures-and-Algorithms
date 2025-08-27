class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False

        if word == "":
            return True

        rows = len(board)
        cols = len(board[0])

        def solve(i, j, k):
            # we found the word
            if k == len(word):
                return True

            # out of bounds or already used or char mismatch
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != word[k]:
                return False                

            # mark visited
            tmp = board[i][j]
            board[i][j] = None

            # explore 4 directions
            found = (
                solve(i+1, j, k+1)
                or solve(i-1, j, k+1)
                or solve(i, j+1, k+1)
                or solve(i, j-1, k+1)
            )

            # restore the cell (Backtrack)
            board[i][j] = tmp
            return found

        for r in range(rows):
            for c in range(cols):
                if solve(r, c, 0):
                    return True
        return False
        