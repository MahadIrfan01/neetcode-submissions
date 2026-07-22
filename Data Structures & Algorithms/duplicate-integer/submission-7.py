class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = []

        for n in nums:
            if n in res:
                return True
            else: 
                res.append(n)
        return False
