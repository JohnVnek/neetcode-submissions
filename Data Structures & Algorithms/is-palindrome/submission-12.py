class Solution:
    def isPalindrome(self, s: str) -> bool:
        # wrd, rev = "", ""
        # for c in s:
        #     c = c.lower()
        #     if (ord(c) - ord("a") in range(26) or ord(c) - ord ("0") in range(10)):
        #         wrd += c
        #         rev = c + rev
        # return wrd == rev
        def valid(c):
            return ((ord(c) - ord("a") in range(26)) or 
                   (ord(c) - ord("A") in range(26)) or
                   (ord(c) - ord("0") in range(10)))

        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not valid(s[l]):
                l += 1
            while r > l and not valid(s[r]):
                r -= 1

            print(s[l].lower(), s[r].lower())
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True