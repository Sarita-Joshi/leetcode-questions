class Solution:
    def trap(self, height: List[int]) -> int:
        
        water = 0
        lmax = height[0]
        rmax = height[-1]
        l=0
        r=len(height)-1
        
        while l < r:
            if lmax < rmax:
                l=l+1
                lmax = max(lmax, height[l])
                water += lmax - height[l]
            else:
                r=r-1
                rmax = max(rmax, height[r])
                water += rmax - height[r]
            
        return water
                
                