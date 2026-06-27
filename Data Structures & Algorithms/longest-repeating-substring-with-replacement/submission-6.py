class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = {}
        count = 1

        l = 0
        r = 0
        n = len(s)

        while r < n:
            hash_map[s[r]] = hash_map.get(s[r], 0) + 1
            while (r-l+1) - max(hash_map.values()) > k:
                hash_map[s[l]] -= 1
                l += 1
            count = max(count, r-l+1)
            print(count)
            r += 1

        return count