class Solution:
    def maxSubArray(self, nums):
        max_sum=nums[0]
        n=nums[0]
        for i in nums[1:]:
            # print(max_sum)
            the_sum=max([i,i+max_sum])

            max_sum=the_sum
            if max_sum>n:
                n=max_sum
        return n
print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
                            # -2,1,-2