# Author:ZJF
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n=len(nums)
        for i in range(n-1,-1,-1):
            print(i)
            if nums[i]==val:
                del nums[i]
        return nums
print(Solution().removeElement([2,1,2,2,3,0,4,2,2,2,2,2,2],2))
