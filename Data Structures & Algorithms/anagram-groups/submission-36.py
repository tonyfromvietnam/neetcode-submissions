class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for string in strs:
            temp = {}
            for i in string:
                temp[i] = temp.get(i, 0) + 1
            
            ans[tuple(sorted(temp.items()))].append(string)
        return list(ans.values())
        