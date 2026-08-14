class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:    
        dict_num = {}
        answer = [[] for i in range(len(nums) + 1)]
        res = []
        
        for num in nums:
            dict_num[num] = dict_num.get(num, 0) + 1
        for n, c in dict_num.items():
            answer[c].append(n)

        for i in range(len(answer) - 1, 0, -1):
            for n in answer[i]:
                res.append(n)
                if len(res) == k:
                    return res
            