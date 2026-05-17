class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS = len(board)
        COLS = len(board[0])

        def capture(R, C):
            if R<0 or C<0 or R>=ROWS or C>=COLS or board[R][C]!="O":
                return 

            board[R][C] = "T"

            capture(R+1,C)
            capture(R-1,C)
            capture(R,C+1)
            capture(R,C-1)

        # 1. Mark all the 'O's to 'T's (unsurrounded region)
        for i in range(ROWS):
            for j in range(COLS):
                if (board[i][j]=='O' and
                    (i in [0, ROWS-1] or j in [0, COLS-1])):
                    capture(i, j)

        # 2. Replace all the 'O's with 'X's
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j]=="O":
                    board[i][j]="X"


        # 3. Replace all the 'T's with 'O'
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j]=="T":
                    board[i][j]="O"
