class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hs = {}

        for n in nums: 
            if n in hs: 
                return True 
            hs[n] = n
        return False