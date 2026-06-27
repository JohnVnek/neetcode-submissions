class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        b = 0
        n = len(nums)-1
        while b <= n:
            middle = (n+b+1) // 2
            print(middle)
            if nums[middle] < target:
                b = middle+1
            elif nums[middle] > target:
                n = middle-1
            else:
                return middle
        return -1