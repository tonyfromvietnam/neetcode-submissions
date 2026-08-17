class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashSet = {}

        for i, n in enumerate(nums):
            if target - n in hashSet:
                return [hashSet[target-n], i]

            hashSet[n] = i
            
        return