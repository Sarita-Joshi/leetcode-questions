class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxl = 0
        numset = set(nums)

        for n in nums:
            if n-1 not in numset:
                l=0
                while n+l in numset:
                    l+=1
                maxl = max(maxl, l)
        return maxl
            
