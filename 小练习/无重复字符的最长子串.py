# Author:ZJF
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)<=1:
            return len(s)
        s=list(s)
        max_num=0
        len_s=len(s)
        start = 0
        end = 0
        while end <= len_s:

            n = end - start
            if n > max_num:
                max_num = n
            a_list = s[start:end + 1]
            if len(a_list) == len(set(a_list)):
                end += 1
            else:
                start += 1
        return max_num
print(Solution().lengthOfLongestSubstring("abcabc"))