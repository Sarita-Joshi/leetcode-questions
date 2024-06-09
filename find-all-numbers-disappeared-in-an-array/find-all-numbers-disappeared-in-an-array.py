class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        a = [0]* n
        
        for i in nums:
            a[i-1] = 1
            
        return [i+1 for i in range(n) if a[i]!=1]