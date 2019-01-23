# Author:ZJF
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        a_dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        sum = 0
        prev = 0
        for i in s:
            if prev < a_dict[i]:
                sum -= 2*prev
            sum+=a_dict[i]
            prev=a_dict[i]
        return sum

print(Solution().romanToInt("VI"))