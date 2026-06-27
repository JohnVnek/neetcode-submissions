class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def bfs(x, y, num):
            for dr, dc in dirs:
                r = x + dr
                c = y + dc
                if (r in range(rows) and c in range(cols) and 
                    ((grid[r][c] == 2147483647) or (grid[r][c] > 0 and num < grid[r][c]))):
                    grid[r][c] = num+1
                    bfs(r, c, num+1)

        for x, r in enumerate(grid):
            for y, c in enumerate(r):
                if c == 0:
                    bfs(x, y, 0)