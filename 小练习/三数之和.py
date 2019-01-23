# Author:ZJF
class Solution(object):
    def threeSum(self, nums):
        m={}
        for i in range(len(nums)):
            m[nums[i]]=i
        l = []
        for a in range(len(nums)):
            for b in range(len(nums)):
                if (a != b) and -(nums[a] + nums[b]) in nums and (a != m[-(nums[a] + nums[b])]) and (b != m[-(nums[a] + nums[b])]):
                    l.append(sorted([nums[a],nums[b],-(nums[a]+nums[b])]))
        return(list(list(t) for t in(set([tuple(t) for t in l]))))



print(Solution().threeSum([0,14,-7,2,7,11,-9,11,-12,6,-10,-8,9,-3,7,-6,3,4,14,-10,-8,5,-1,6,12,9,12,-11,-15,-5,5,0,-6,13,9,9,10,7,5,13,-2,11,-10,-15,-15,4,-14,-4,-15,7,-7,-15,-3,8,-2,-13,-6,-5,-9,-14,5,12,1,6,2,-12,-8,-11,10,13,-13,-14,1,14,8,1,-4,9,4,-12,-6,13,10,6,6,-7,8,7,3,7,8,-15,-4,-14,-1,13,-11,6,-12,-15,4,12,8,-10,4,1,-1,7,-13,-12,10,-4,8,6,10,-1,6,-5,13,-13,9,6,-13,-10]))

