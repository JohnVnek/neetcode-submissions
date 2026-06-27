class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Create two queues
        # Queue 1: CurrQueue
        # Queue 2: ChildQueue

        # Maintain set -> currently added pairs dont get readded

        # Will start BFS once we find the first "2" in the 2D array

        currQueue = deque()
        childQueue = deque()
        m = len(grid)-1
        n = len(grid[0])-1

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        time = 0

        for r_idx, row in enumerate(grid):
            for c_idx, col in enumerate(row):
                if col == 2:
                    coords = [r_idx, c_idx]
                    currQueue.append(coords)
        
        while currQueue:
            curr = currQueue.popleft()
            for direc in directions:
                row = curr[0] + direc[0]
                col = curr[1] + direc[1]
                if row < 0 or row > m or col < 0 or col > n:
                    continue
                
                print(row)
                print(col)
                if grid[row][col] == 1:
                    grid[row][col] = 2
                    coord = [row, col]
                    childQueue.append(coord)
            if not currQueue and childQueue:
                time += 1
                temp = childQueue
                childQueue = currQueue
                currQueue = temp

        for r_idx, row in enumerate(grid):
            for c_idx, col in enumerate(row):
                if col == 1:
                    return -1
        return time
                    
                

