class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        
        res = 0              

        for num in nums:
            if num - 1 not in nums:
                current_length = 1
                while num + current_length in numSet:
                    current_length += 1
                res = max(res, current_length)

        return res