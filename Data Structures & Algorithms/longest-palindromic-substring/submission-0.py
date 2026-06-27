class Solution:
    def longestPalindrome(self, s: str) -> str:
        # O(n^2)

        n = len(s)

        res_len = 0
        res_idx = 0

        dp = [[False for i in range(n)] for j in range(n)]

        for l in range(n-1, -1, -1):
            for r in range(l, n):
                if s[l] == s[r] and (r-l+1 <= 2 or dp[l+1][r-1]):
                    dp[l][r] = True
                    if res_len < r-l+1:
                        res_len = r-l+1
                        res_idx = l
        return s[res_idx : res_idx+res_len]

        