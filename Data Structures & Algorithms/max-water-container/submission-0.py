class Solution:
    def maxArea(self, heights: List[int]) -> int:
        size = len(heights)
        left, right = 0, size-1
        area = 0

        while not left == right:
            l_height = heights[left]
            r_height = heights[right]
            curr = min(l_height, r_height) * (right-left)
            area = max(area, curr)

            if l_height < r_height:
                left += 1
            else:
                right -= 1
        return area