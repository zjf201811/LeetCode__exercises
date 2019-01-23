# Author:ZJF
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # nums=list(set(nums))
        nums.sort()
        res = []
        lennums = len(nums)

        for i in range(lennums):
            left = i + 1
            right = lennums - 1

            if i > 0 and nums[i - 1] == nums[i]:

                continue

            while left < right:
                sumthree = nums[i] + nums[left] + nums[right]
                if sumthree == 0:
                    res_col = [nums[i], nums[left], nums[right]]
                    res.append(res_col)
                    left += 1
                    right -= 1

                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                    while nums[right] == nums[right + 1] and left < right:
                        right -= 1

                if sumthree < 0:
                    left += 1
                if sumthree > 0:
                    right -= 1
        print(nums)
        return res
# print(Solution().threeSum([0,-15,4,-9,-14,5,4,-12,-6,13,10,6,6,-14,-1,13,-11,6,-12,-15,4,12,8,-10,4,1,-1,7,-13,-12,10,-4,8,6,10,-1,6,-5,13,-13,9,6,-13,-10]))
print(Solution().threeSum([-1,0,1,2,-1,-4]))