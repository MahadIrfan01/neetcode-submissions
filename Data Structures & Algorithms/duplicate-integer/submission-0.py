class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = set()
        for i in range(len(nums)):
            if nums[i] not in hash_map:
                hash_map.add(nums[i])
            elif nums[i] in hash_map:
                return True 
     
        return False

 
            
            
                
            
            


            