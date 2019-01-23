# Author:ZJF
class Solution:
    def __init__(self):
        self.count = 0
        self.number_list = []
    def is_coincide(self, list1, list2):
        if "".join(list1).isdigit():
            return False
        else:
            for (m, n) in zip(list1, list2):  # 切出来的和印章匹配
                if m != n and m != "0":
                    return False
            else:
                return True
    # def is_digit(self, a_list):     # 判断一个列表是否由纯数字组成
    #     the_str = "".join(a_list)
    #     return the_str.isdigit()
    def movesToStamp(self, stamp, target):
        m = len(stamp)
        n = len(target)
        stamp_list = list(stamp)
        target_list = list(target)
        while True:
            if "".join(target_list).isdigit():
                self.number_list.reverse()
                print(self.count)
                return self.number_list
            if self.count>10:
                print(self.count)
                return[]
            else:
                self.count += 1
            for i in range(n-m+1):           #  补全印章
                the_list = target_list[i:i + m]
                if self.is_coincide(the_list, stamp_list):
                    self.number_list.append(i)
                    target_list[i:i+m] = ["0"]*m
