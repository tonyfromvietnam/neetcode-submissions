class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        
        # 1. Build prefix product in output
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]
        
        # 2. Multiply by suffix product
        suffix = 1
        for i in range(n-1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
        
        return output