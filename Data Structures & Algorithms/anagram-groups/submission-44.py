class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for string in strs:
            temp = [0] * 26
            for i in string:
                temp[ord('a') - ord(i)] += 1
            
            ans[tuple(temp)].append(string)

        return list(ans.values())