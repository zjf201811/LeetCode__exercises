class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        new_str = ""
        if str == '' or str == '+' or str == '-':
            return 0
        if str[0] == "+" or str[0] == "-" or str[0].isdigit():
            new_str += str[0]
        else:
            return 0
        try:
            for i in str[1:]:
                if i.isdigit():
                    new_str += i
                else:
                    break
            int_str=int(new_str)
            if int_str>2**31-1:
                return 2**31-1
            if int_str<-2**31:
                return -2**31
            return int_str
        except:
            return 0
