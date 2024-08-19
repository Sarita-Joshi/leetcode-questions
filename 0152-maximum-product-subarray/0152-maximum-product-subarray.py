class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        lefttoright=1
        righttoleft=1
        
        ans = nums[0]
        n = len(nums)
        for i in range(n):
            if lefttoright==0:
                lefttoright=1
            if righttoleft==0:
                righttoleft=1
            
            lefttoright *= nums[i]
            righttoleft *= nums[n-i-1]
            
            ans = max(ans, max(lefttoright, righttoleft))
        return ans
            