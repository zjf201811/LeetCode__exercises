# Author:ZJF
class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        nums_dict = {}
        for x in range(n):
            a = target - nums[x]
            if nums[x] in nums_dict:

                return list((nums_dict[nums[x]], x))
            else:
                nums_dict[a] = x

print(Solution().twoSum([2, 7, 11, 15], 9))
