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

        # Depth First Search
        def dfs(r, c):
            q = collections.deque()
            dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            visited.add((r, c))
            q.append((r, c))

            while len(q) != 0:
                curr = q.pop()
                for dr, dc in dirs:
                    x = curr[0] + dr
                    y = curr[1] + dc
                    if x in range(rows) and y in range(cols) and grid[x][y] == "1" and (x, y) not in visited:
                        visited.add((x, y))
                        q.append((x, y))


        def dfs_recur(x, y):
            if x in range(rows) and y in range(cols) and grid[x][y] == "1" and (x, y) not in visited:
                visited.add((x, y))
                dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                for dr, dc in dirs:
                    dfs_recur(x+dr, y+dc)

        for x, r in enumerate(grid):
            for y, c in enumerate(r):
                if grid[x][y] == "1" and (x, y) not in visited:
                    # bfs(x, y)
                    # dfs(x, y)
                    dfs_recur(x, y)
                    islands += 1

        return islands
                
    # def numIslands(self, grid: List[List[str]]) -> int:




            