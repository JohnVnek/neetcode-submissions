class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()

        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        # Breadth First Search 
        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))
            dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

            while len(q) != 0:
                curr = q.popleft()
                for dr, dc in dirs:
                    x = curr[0] + dr
                    y = curr[1] + dc
                    if x in range(rows) and y in range(cols) and grid[x][y] == "1" and (x, y) not in visited:
                        visited.add((x, y))
                        q.append((x, y))

        for x, r in enumerate(grid):
            for y, c in enumerate(r):
                if grid[x][y] == "1" and (x, y) not in visited:
                    bfs(x, y)
                    islands += 1

        return islands
                
        


            