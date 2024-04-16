class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = nums[0]
        for i in nums[1:]:
            if n == i:
                nums.remove(n)
            else:
                n = i
        return len(nums)

    ## Two pointer approach
        # i = 0
        # for j in nums[1:]:
        #     if nums[i]!=j:
        #         i=i+1
        #         nums[i] = j
        # return i+1