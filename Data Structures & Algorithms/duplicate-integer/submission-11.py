class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hs = {}

        for i in range(len(nums)): 
            if nums[i] in hs: 
                return True 
            hs[nums[i]] = nums[i]
        return False