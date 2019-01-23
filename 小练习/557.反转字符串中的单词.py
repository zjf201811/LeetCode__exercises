# Author:ZJF
class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        str_list=s.split(" ")
        for i in range(len(str_list)):
            str_list[i]=str_list[i][-1::-1]
        return " ".join(str_list)
print(Solution().reverseWords("12 12 12"))