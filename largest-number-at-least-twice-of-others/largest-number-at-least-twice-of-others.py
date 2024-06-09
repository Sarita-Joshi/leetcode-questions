class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxv = max(nums)
        maxi=0
        for i in range(len(nums)):
            if nums[i]==maxv:
                maxi = i
            elif nums[i]*2> maxv:
                return -1
        return maxi