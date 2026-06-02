class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # iterate over graph to find island
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                cell = grid[row][col]
                if cell == 1:
                    # calculate perimeter
                    # if solo island -> p = 4
                    # if two connections -> p += 2
                    # if one connection -> p += 3
                    return self.bfs(row, col, grid)
                # print('checking')
        return 0

    def bfs(self, row, col, grid) -> int:
        # directions = [[0,1],[1,0],[0,-1],[-1,0]]
        queue = [(row,col)]
        perimeter = 0
        while queue:
            # print(queue, perimeter)
            current_row, current_col = queue[0]
            print(queue[0], grid)
            del queue[0]
            grid[current_row][current_col] = -1
            neighbor_count = 0
            # count and enqueue neighbors
            if current_row+1 < len(grid) and grid[current_row+1][current_col] != 0:
                neighbor_count += 1
                if grid[current_row+1][current_col] == 1:
                    queue.append((current_row+1, current_col))
                    grid[current_row+1][current_col] = -1
            if current_row-1 >= 0 and grid[current_row-1][current_col] != 0:
                neighbor_count += 1
                if grid[current_row-1][current_col] == 1:
                    queue.append((current_row-1, current_col))
                    grid[current_row-1][current_col] = -1
            if current_col+1 < len(grid[current_row]) and grid[current_row][current_col+1] != 0:
                neighbor_count += 1
                if grid[current_row][current_col+1] == 1:
                    queue.append((current_row, current_col+1))
                    grid[current_row][current_col+1] = -1
            if current_col-1 >= 0 and grid[current_row][current_col-1] != 0:
                neighbor_count += 1
                if grid[current_row][current_col-1] == 1:
                    queue.append((current_row, current_col-1))
                    grid[current_row][current_col-1] = -1

            if neighbor_count == 0:
                # print('onceeee')
                return 4
            elif neighbor_count == 2:
                perimeter += 2
            elif neighbor_count == 3:
                perimeter += 1
            elif neighbor_count == 1:
                perimeter += 3

            
            # print(grid, )
        return perimeter