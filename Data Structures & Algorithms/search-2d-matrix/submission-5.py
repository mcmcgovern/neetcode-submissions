class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # brute force
        for row in range(len(matrix)):
            for val in matrix[row]:
                if val == target:
                    return True
        return False