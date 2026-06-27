class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i, n in enumerate(nums):
            if n not in indices:
                indices[n] = i
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [indices[diff], i]

        return []