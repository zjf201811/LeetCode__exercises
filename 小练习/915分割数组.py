# Author:ZJF
class Solution(object):
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        left=[]
        left.append(A.pop(0))
        while max(left) > min(A):

            left.append(A.pop(0))
            if len(A) == 0:
                return 0
        return len(left)
print(Solution().partitionDisjoint([1, 1]))
