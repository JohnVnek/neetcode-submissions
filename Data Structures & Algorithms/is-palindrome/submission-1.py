class Solution:
    def isPalindrome(self, s: str) -> bool:
        wrd, rev = "", ""
        for c in s:
            c = c.lower()
            if (ord(c) - ord("a") in range(26) or ord(c) - ord ("0") in range(10)):
                wrd += c
                rev = c + rev
        return wrd == rev