class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = defaultdict(list)
        
        for s in strs:
            temp[tuple(sorted(s))].append(s)

        return list(temp.values())
