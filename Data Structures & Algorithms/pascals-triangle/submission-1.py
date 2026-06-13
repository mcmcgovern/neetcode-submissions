class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1]]
        if numRows == 1:
            return rows

        for i in range(1, numRows):
            row = [1]
            # starting with 3rd row (i=2), include i-2 inner cells
            for inner in range(i-1):
                row.append(rows[i-1][inner] + rows[i-1][inner+1])
            row.append(1)
            rows.append(row)
        return rows