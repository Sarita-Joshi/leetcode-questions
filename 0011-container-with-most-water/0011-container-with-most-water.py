class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l=0
        r=len(height) -1
        
        max_water = 0
        
        while l<r:
                
            water = (r-l) * min(height[l], height[r])
            if water > max_water:
                max_water = water
            if height[l] > height[r]:
                r-=1
            else:
                l+=1
                
        
        return max_water
            