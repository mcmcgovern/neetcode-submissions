class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1]]
        for i in range(1, numRows):
            row = [1]
            for l in range(i-1):
                row.append(rows[i-1][l] + rows[i-1][l+1])
            row.append(1)
            rows.append(row)
        return rows