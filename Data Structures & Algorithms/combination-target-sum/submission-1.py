class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sums = []

        def backtrack(i, total):
            if total == target:
                res.append(sums.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            sums.append(nums[i])
            backtrack(i, total+nums[i])
            sums.pop()
            backtrack(i+1, total)

        
        backtrack(0, 0)
        return res
                
            