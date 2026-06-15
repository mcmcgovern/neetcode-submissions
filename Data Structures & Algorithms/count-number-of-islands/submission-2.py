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
        while queue:
            (r,c) = queue.popleft()
            grid[r][c] = 'V' # mark as visited

            if r+1 < len(grid) and grid[r+1][c] == '1':
                queue.append((r+1,c))
            if r-1 >= 0 and grid[r-1][c] == '1':
                queue.append((r-1,c))
            if c+1 < len(grid[r]) and grid[r][c+1] == '1':
                queue.append((r,c+1))
            if c-1 >= 0 and grid[r][c-1] == '1':
                queue.append((r,c-1))





