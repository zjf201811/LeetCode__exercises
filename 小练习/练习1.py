#Author:ZJF
list1 = [5, 3, 2, 8, 1, 4]


# def sort_array(arr):
#     odd_index = [ind for (ind,val) in enumerate(arr) if val%2 ==1]
#     sorted_odd = sorted([odd for odd in arr if odd%2==1])
#     j=0
#     for i in odd_index:
#         arr[i]=sorted_odd[j]
#         j+=1
#     return arr if arr!=[] else[]
# print(sort_array([1,4,8,5,43,6,8,9]))


# def sort_array(arr):
#     odds = [x if x%2==0 else 0 for x in arr]
#     evens = sorted([x for x in arr if x%2==1])
#     event_index = 0
#     for index,e in enumerate(odds):
#         if e==0:
#             odds[index]=evens[event_index]
#             event_index+=1
#     return odds
# print(sort_array(list1))


def sort_array(arr):
    odds = sorted((x for x in arr if x%2!=0),reverse=True)
    print([x if x%2==0 else odds.pop() for x in arr])
sort_array(list1)