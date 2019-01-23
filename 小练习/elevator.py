# Author:ZJF
import random

all = [2, 3, 4, 5, 6, 7]
elevator_list = []
all_list = []

def split(list):
    return[[list[0],list[1]], [list[1],list[2]], [list[0], list[2]] ]

for a in range(2,8):
    for b in range(2,8):
        for c in range(2,8):
            if len(set([a,b,c])) == 3:
                list2 = [a, b, c]
                list2.sort()
                if list2 not in elevator_list:
                    elevator_list.append(list2)

for i in range(2,8):
    for j in range(2,8):
        if i != j:
            list3=[i,j]
            list3.sort()
            if list3 not in all_list:
                list3.sort()
                all_list.append(list3)

n = int(input("请输入电梯数量:"))
new_list = []
num = 0
for i in range(10000):
    z = random.sample(elevator_list, n)
    for i in z:
        new_list.extend(split(i))
    for i in all_list:
        if i not in new_list:

            new_list.clear()
            break
    else:
        print("这个行")
        num += 1
        print(z)
        new_list.clear()
print("找到%s种解法"%num)
if num == 0:
    print("都不行")