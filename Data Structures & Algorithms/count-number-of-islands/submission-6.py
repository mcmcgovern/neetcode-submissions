class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        ROWS, COLS = len(grid), len(grid[0])
        # iterate over grid until land is found
        # perform bfs iterating over neighbors
        # increment count

        def dfs(r,c):
            grid[r][c] = '-1'
            queue = deque()
            queue.append((r,c))
            while queue:
                # pop element and check its neighbors
                row, col = queue.popleft()
                if 0 <= row+1 < ROWS and grid[row+1][col] == '1':
                    queue.append((row+1, col))
                    grid[row+1][col] = '-1'
                if 0 <= col+1 < COLS and grid[row][col+1] == '1':
                    queue.append((row, col+1))
                    grid[row][col+1] = '-1'
                if 0 <= row-1 < ROWS and grid[row-1][col] == '1':
                    queue.append((row-1, col))
                    grid[row-1][col] = '-1'
                if 0 <= col-1 < COLS and grid[row][col-1] == '1':
                    queue.append((row, col-1))
                    grid[row][col-1] = '-1'
                # mark as visited so we do not try again
                # grid[row][col] = '-1'

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '1':
                    dfs(row,col)
                    count += 1

        return count