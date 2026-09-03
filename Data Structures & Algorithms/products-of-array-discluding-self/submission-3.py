class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        res = [1] * len(nums)

        for i in range(len(nums)):
            res[i] = product
            product *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i] 

        return res