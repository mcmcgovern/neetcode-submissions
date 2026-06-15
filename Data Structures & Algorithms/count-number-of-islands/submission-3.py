class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # do grid traversal until land is found
        island_count = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1":
                    island_count += 1
                    # do BFS
                    self.bfs(grid, r, c)

        return island_count

    def bfs(self, grid, row, col):
        queue = deque()
        queue.append((row,col))
        grid[row][col] = 'V' # mark as visited
        while queue:
            (r,c) = queue.popleft()

            if r+1 < len(grid) and grid[r+1][c] == '1':
                grid[r+1][c] = 'V'
                queue.append((r+1,c))
            if r-1 >= 0 and grid[r-1][c] == '1':
                grid[r-1][c] = 'V'
                queue.append((r-1,c))
            if c+1 < len(grid[r]) and grid[r][c+1] == '1':
                grid[r][c+1] = 'V'
                queue.append((r,c+1))
            if c-1 >= 0 and grid[r][c-1] == '1':
                grid[r][c-1] = 'V'
                queue.append((r,c-1))





