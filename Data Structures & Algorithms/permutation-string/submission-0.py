class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = [0] * 26
        for c in s1:
            s1_map[ord(c) - ord('a')] += 1
        
        l = 0
        s2_map = [0] * 26
        # Check that s1_map and s2_map are equal
        # If equal at any point, return true
        for r in range(len(s2)):
            s2_map[ord(s2[r]) - ord('a')] += 1
            if r-l+1 == len(s1):
                if s1_map == s2_map:
                    return True
                else: 
                    if s2_map[ord(s2[l]) - ord('a')] >= 0:
                        s2_map[ord(s2[l]) - ord('a')] -= 1
                    l += 1
        return False
