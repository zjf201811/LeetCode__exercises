# Author:ZJF
class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return 0
        elif len(nums)==2:
            return nums.index(max(nums))

        for i in range(1,len(nums)-1):
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                return i
        else:return None