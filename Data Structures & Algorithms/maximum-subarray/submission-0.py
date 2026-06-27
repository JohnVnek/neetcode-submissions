class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        curr_max = float('-inf')
        curr = 0
        for num in nums:
            curr += num
            curr_max = max(curr_max, curr)
            if curr < 0:
                curr = 0
                
        return curr_max
        