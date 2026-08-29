class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first we need to find which row target WOULD be in if present
        # do binary search on rows
        low, high = 0, len(matrix)-1
        while low <= high:
            row = low + (high-low) // 2
            if matrix[row][0] <= target <= matrix[row][len(matrix[row])-1]:
                break
            elif matrix[row][0] > target:
                high = row - 1
            else:
                low = row + 1

        print(row)
        # we know row for sure
        low, high = 0, len(matrix[row]) - 1
        while low <= high:
            col = low + (high-low) // 2
            # if low == high and matrix[row][col] != target:
            #     return False
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                high = col - 1
            else:
                low = col + 1
        return False