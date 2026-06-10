class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first find row range of target, starting from mid row
        # len(matrix) is the number of rows
        low, high = 0, len(matrix)-1
        row = -1
        while low <= high:
            mid = (low+high)//2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = mid
                break
            elif matrix[mid][0] > target:
                high = mid - 1
            elif matrix[mid][-1] < target:
                low = mid + 1

        if row == -1:
            return False

        # next do regular binary search in found row [0, 3], m=1
        low, high = 0, len(matrix[row])-1
        while low <= high:
            mid = (low+high)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False