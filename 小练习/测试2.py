# Author:ZJF
class Solution:
    def reverse(self, x):
        sign=1
        # if x>2**31-1 or x<-2**31:
        #     return 0
        if x<0:
            sign=-1
            x=-x
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        n = len(x)
        new_x = ""
        for i in range(n-1,0-1,-1):
            new_x+=x[i]
        x = int(new_x)*sign
        return 0 if x>2**31-1 or x<-2**31 else x
print(Solution().reverse(1234))