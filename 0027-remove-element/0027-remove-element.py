class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            if nums[i] == val:
                count+=1
            elif i>=count and count>0:
                nums[i-count] = nums[i]


        return len(nums)-count