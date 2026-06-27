class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): 
            return False
        
        s1_chars = [0]*26
        s2_chars = [0]*26

        for i, s in enumerate(s1):
            s1_chars[ord(s) - ord('a')] += 1
            # print(s1_chars)
            s2_chars[ord(s2[i]) - ord('a')] += 1
            # print(s2_chars)
        
        behind = 0
        for i in range(len(s1), len(s2)):
            if s1_chars == s2_chars:
                return True
            s2_chars[ord(s2[behind]) - ord('a')] -= 1
            behind += 1
            s2_chars[ord(s2[i]) - ord('a')] += 1
            
        if s1_chars == s2_chars:
                return True
        return False


