# Author:ZJF
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        return True if int(str(x)[-1::-1])==x else False

