class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_fix, post_fix, res = [], [], []
        i, j = 0, len(nums)-1
        max_len = len(nums)

        while i < max_len:
            if (len(pre_fix) == 0):
                pre_fix.append(nums[i])
                post_fix.append(nums[j])
            else:
                pre_fix.append(nums[i]*pre_fix[i-1])
                post_fix.append(nums[j]*post_fix[i-1])
            i += 1
            j -= 1
        post_fix.reverse()
        
        for r in range(max_len):
            pre, post = 1, 1
            if r-1 in range(max_len):
                pre = pre_fix[r-1]
            if r+1 in range(max_len):
                post = post_fix[r+1]
            res.append(pre*post)
        return res
