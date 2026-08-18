class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:    
        temp = {}
        store = [[] for i in range(len(nums) + 1)]

        for i in nums:
            temp[i] = temp.get(i, 0) + 1

        for i, v in temp.items():
            store[v].append(i)

        ans = []
        for i in range(len(store) - 1, 0, -1):            
            for val in store[i]:
                ans.append(val)
                if len(ans) == k:
                    return ans