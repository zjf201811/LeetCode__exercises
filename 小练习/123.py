# Author:ZJF
class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        nums_dict = {}
        for x in range(n):
            a = target - nums[x]
            if nums[x] in nums_dict:
                print(nums_dict)
                return list((nums_dict[nums[x]], x, nums[nums_dict[nums[x]]], nums[x]))
            else:
                nums_dict[a] = x
print(Solution().twoSum([16021, 0], 16021))