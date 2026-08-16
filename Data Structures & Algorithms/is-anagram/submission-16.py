class Solution:
    def isAnagram(self, s: str, t: str) -> bool:        
        dict_s, dict_t = [0]*26, [0]*26

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            dict_s[ord(s[i]) - ord('a')] += 1
            dict_t[ord(t[i]) - ord('a')] += 1
        
        return dict_s == dict_t