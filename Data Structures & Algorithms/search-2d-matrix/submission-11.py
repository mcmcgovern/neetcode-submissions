class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        low, high = 0, ROWS*COLS - 1

        while low <= high:
            mid = low + (high-low) // 2
            # perform calculation using mod to get row, col
            # mid is a index in range 0-11, let's say 5
            # if mid is in the second row then row = mid // COLS
                # 7 // 4 = 1... CORRECT
            # if mid is in the second col then col = mid % COLS
                # 5 mod 4 = 1... CORRECT
            row, col = mid // COLS, mid % COLS
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False