class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set()

        for n in nums:
            nums_set.add(n)

        total = 0
        for n in nums_set:
            count = 1
            if n-1 not in nums_set:
                next = n+1
                while next in nums_set:
                    count += 1
                    next += 1
            if count > total:
                total = count

        return total
        