class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        
        res = 0
        current_length = 0         

        for num in nums:
            if num - 1 not in nums:
                current_length = 1
                while num + 1 in numSet:
                    current_length += 1
                    num += 1
                res = max(res, current_length)

        return max(res, current_length)