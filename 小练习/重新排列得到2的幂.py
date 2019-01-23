# Author:ZJF
class Solution:
    def reorderedPowerOf2(self, N):
        number_list = [str(2**i) for i in range(30)]
        for x in number_list:
            if len(str(N))==len(x) and set(str(N))==set(x):
                return True
        else:
            return False
print(Solution().reorderedPowerOf2(10424))
