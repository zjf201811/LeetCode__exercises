# Author:ZJF
# 输入：stamp = "abc", target = "ababc"
# 输出：[0,2]
# （[1,0,2] 以及其他一些可能的结果也将作为答案被接受）
# 示例 2：
#
# 输入：stamp = "aabcaca", target = "abca"
# 输出：[3,0,1]
import random

def movesToStamp(stamp, target):

    m = len(stamp)
    n = len(target)
    the_str = n*["?"]
    times = n-m+1
    list2 = [x for x in range(times)]
    for i in range(10000):
        random.shuffle(list2)
        # list2 = [1,0,2]
        for i in list2:
            for j in range(m):
                the_str[i] = stamp[j]
                i += 1
        if the_str == list(target):

            return list2

    else:
        return []


print(movesToStamp("aq","aqaaqaqqqaqqaaq"))






