class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [[1,0], [0,1], [-1,0], [0, -1]]
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        
        def explore(x, y):
            grid[y][x] = "2"
            for dx, dy in dirs:
                if (y+dy >= 0 and y+dy < rows) and (x+dx >= 0 and x+dx < cols):
                    if grid[y+dy][x+dx] == "1":
                        print(x+dx)
                        print(y+dy)
                        print()
                        explore(x+dx, y+dy)


        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                if val == "1":
                    # print(x)
                    # print(y)
                    # print(val)
                    # print()
                    explore(x, y)
                    count += 1

        
        return count

