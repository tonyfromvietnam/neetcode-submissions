class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:    
        freq = {}
        lst = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for number, count in freq.items():
            lst[count].append(number)

        answer = []
        for i in range(len(lst) - 1, 0, -1):
            for n in lst[i]:
                answer.append(n)
                if len(answer) == k:
                    return answer