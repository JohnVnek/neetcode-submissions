class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        total = 0

        def bfs(x, y):
            q = collections.deque()
            count = 1
            visited.add((x, y))
            q.append((x, y))
            dirs = [[1,0], [0,1], [-1,0], [0,-1]]

            while len(q) != 0:
                curr = q.popleft()
                for dr, dc in dirs:
                    x = curr[0] + dr
                    y = curr[1] + dc
                    if x in range(rows) and y in range(cols) and grid[x][y] == 1 and (x, y) not in visited:
                        q.append((x, y))
                        visited.add((x, y))
                        count += 1
            return count

        for x, r in enumerate(grid):
            for y, c in enumerate(r):
                if grid[x][y] == 1 and (x, y) not in visited:
                    count = bfs(x, y)
                    if count > total:
                        total = count

        return total