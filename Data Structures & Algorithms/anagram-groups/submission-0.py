class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}  # Dictionary to store grouped anagrams

        for word in strs:
            # Create a frequency count for each lowercase letter (assumes a-z only)
            count = [0] * 26  
            for c in word:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)  # Use tuple as dictionary key
            
            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = [word]
        
        return list(anagrams.values())