class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        current_max_area = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        directions = [
            [1,0],
            [0,1],
            [-1,0],
            [0,-1]
        ]

        def dfs(row, col, area) -> int:
            queue = deque()
            queue.append((row, col))
            while queue:
                r,c = queue.popleft()
                for d in directions:
                    row_plus, col_plus = d
                    nr, nc = r + row_plus, c + col_plus
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 0 # mark as visited
                        queue.append((nr, nc))
                        area += 1
            return area

        # find islands
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    grid[row][col] = 0 # mark as visited
                    current_max_area = max(current_max_area, dfs(row, col, 1))
        return current_max_area