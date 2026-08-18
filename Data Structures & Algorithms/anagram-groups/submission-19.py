class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = defaultdict(list)
        
        for s in strs:
            hash_list = [0] * 26

            for i in s:
                hash_list[ord('a') - ord(i)] += 1
            
            temp[tuple(hash_list)].append(s)

        return list(temp.values())
