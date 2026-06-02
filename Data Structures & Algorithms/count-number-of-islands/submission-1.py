class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # perform BFS, mark visited as V
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                cell = grid[row][col]
                # print(cell)
                if cell == '1':
                    grid = self.bfs(row, col, grid)
                    count += 1
        return count

    def bfs(self, r: int, c: int, grid: List[List[str]]) -> List[List[int]]:
        queue = [(r,c)]
        while queue:
            # print(queue)
            # pop from queue
            current_row, current_col = queue[0]
            del queue[0]
            # north
            if current_col+1 < len(grid[current_row]) and grid[current_row][current_col+1] == '1':
                queue.append((current_row, current_col+1))
            # south
            if current_col-1 >= 0 and grid[current_row][current_col-1] == '1':
                queue.append((current_row, current_col-1))
            # east
            if current_row+1 < len(grid) and grid[current_row+1][current_col] == '1':
                queue.append((current_row+1, current_col))
            # west
            if current_row-1 >= 0 and grid[current_row-1][current_col] == '1':
                queue.append((current_row-1, current_col))
            grid[current_row][current_col] = 'V'
            # print(grid)
        return grid