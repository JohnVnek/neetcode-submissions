class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        n = len(height)
        left = 0
        maxL = height[left]
        right = n-1
        maxR = height[right]

        while left < right:
            if maxL < maxR:
                left += 1
                maxL = max(maxL, height[left])
                res += maxL - height[left]
            else:
                right -= 1
                maxR = max(maxR, height[right])
                res += maxR - height[right]
        return res




