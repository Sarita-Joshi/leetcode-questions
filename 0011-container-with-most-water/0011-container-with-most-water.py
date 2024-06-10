class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        lmax = height[0]
        rmax = height[-1]
        
        l=0
        r=len(height) -1
        
        max_water = 0
        
        while l<r:
                
            water = (r-l) * min(lmax, rmax)
            if water > max_water:
                max_water = water
            if lmax > rmax:
                r-=1
                rmax = max(rmax, height[r])
                
            else:
                l+=1
                lmax = max(lmax, height[l])
                
        
        return max_water
            