class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        s = len(nums)-1
        for i, n in enumerate(nums):
            j = i+1
            k = s
            while j < k:
                three_sum = n + nums[j] + nums[k]
                if three_sum > 0:
                    k -= 1
                elif three_sum < 0:
                    j += 1
                else:
                    add = [n, nums[j], nums[k]]
                    if add not in res:
                        res.append(add)
                    j += 1
        return res
                

        