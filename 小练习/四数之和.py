# Author:ZJF
class Solution:

    def fourSum(self, nums, target):
        t = 0
        res = set()
        dict = {}
        nums_len=len(nums)
        nums.sort()
        for i in range(nums_len):
            for j in range(i+1, nums_len):
                key = nums[i]+nums[j]
                if key in dict:
                    dict[key].append((i,j))
                    print(dict)
                else:
                    dict[key] = [(i, j)]
        for i in range(nums_len):
            for j in range(i+1,nums_len-2):
                exp = target - nums[i]-nums[j]
                if exp in dict:
                    for x in dict[exp]:
                        if x[0]>j:
                            res.add((nums[i],nums[j],nums[x[0]],nums[x[1]]))
                            print(res)

        return[list(i) for i in res]
print(Solution().fourSum([1,0,-1,0,-2,2],0))
# print(Solution().fourSum([0,0,0,0],1))
