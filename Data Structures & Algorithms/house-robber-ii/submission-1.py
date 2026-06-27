class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def dp(start, end, nums):
            max1, max2, = 0, 0
            for i in range(start, end):
                temp = max(max1+nums[i], max2)
                max1 = max2
                max2 = temp
            return max2

        return max(dp(0, n-1, nums), dp(1, n, nums))