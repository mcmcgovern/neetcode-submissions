class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row is valid
        for i in range(len(board)):
            row = board[i]
            if not self.row_is_valid(row):
                return False

        # check col is valid
        for i in range(9):
            if not self.col_is_valid(board, i):
                return False

        # check box is valid
        box_starts = [
            (0,0),
            (0,3),
            (0,6),
            (3,0),
            (3,3),
            (3,6),
            (6,0),
            (6,3),
            (6,6)
        ]

        for start in box_starts:
            if not self.box_is_valid(board, start):
                return False
        return True
    
    def row_is_valid(self, row) -> bool:
        seen = set()
        for cell in row:
            if cell == '.':
                continue
            if cell in seen or cell > '9' or cell < '1':
                return False
            seen.add(cell)
        return True

    def col_is_valid(self, board, index) -> bool:
        seen = set()
        for i in range(9):
            cell = board[i][index]
            if cell == '.':
                continue
            if cell in seen or cell > '9' or cell < '1':
                return False
            seen.add(cell)
        return True

    def box_is_valid(self, board, start) -> bool:
        row, col = start
        seen = set()
        for i in range(3):
            for j in range(3):
                cell = board[row+i][col+j]
                if cell == '.':
                    continue
                if cell in seen or cell > '9' or cell < '1':
                    return False
                seen.add(cell)
        return True
        