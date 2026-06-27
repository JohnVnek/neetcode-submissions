class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        
        start_row = -1
        t, b = 0, rows-1
        while t <= b:
            middle = (t+b+1) // 2
            if matrix[middle][0] > target:
                b = middle-1
            elif matrix[middle][cols-1] < target:
                t = middle+1
            else:
                start_row = middle
                break
        if start_row == -1:
            return False

        l, r = 0, cols-1
        while l <= r:
            middle = (l+r+1) // 2
            if matrix[start_row][middle] > target:
                r = middle-1
            elif matrix[start_row][middle] < target:
                l = middle+1
            else:
                return True
        return False