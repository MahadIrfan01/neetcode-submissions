class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        res = len(nums) * [1]

        for i in range(len(nums)):
            res[i] = product
            product *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1 , -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
        #[1,2,4,3]
        #pref[1,1,2,8]
        #post[24,12,3,1]
        #[24,12,6,8]
