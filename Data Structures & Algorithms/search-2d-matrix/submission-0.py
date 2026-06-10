class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        linear_list = [matrix[row][col] for row in range(len(matrix)) for col in range(len(matrix[row]))]

        low, high = 0, len(linear_list)-1
        while low <= high:
            mid = (low+high)//2
            if linear_list[mid] == target:
                return True
            elif linear_list[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False