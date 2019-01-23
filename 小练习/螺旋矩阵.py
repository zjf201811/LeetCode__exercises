# Author:ZJF
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        the_list=[]
        while len(matrix)!=0:
            n = matrix.pop(0)
            the_list+=n
            matrix = list(map(list,zip(*matrix)))
            matrix.reverse()
        return the_list

s = Solution()
print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))