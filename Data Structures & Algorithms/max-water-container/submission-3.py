class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        #[1,8,6,2,5,4,8,3,7]
        r = len(height) - 1
        l = 0 
        max_w = 0

        while l < r: 
            width = min(height[r], height[l])
            length = r - l
            if height[r] < height[l]:
                r-=1
            else:
                l+=1
            max_w = max(max_w, (length * width))

        return max_w