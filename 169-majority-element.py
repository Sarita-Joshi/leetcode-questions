class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = []
        l = len(nums) // 2
        for i in nums:
            if i not in count:
                count.append(i)
                if nums.count(i) > l:
                    return i
        return 0    
