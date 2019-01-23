# Author:ZJF
class Solution:
    def advantageCount(self, A, B):
        A.sort()
        C=[]
        for i in B:
            for j in A:
                if j>i:
                    C.append(j)
                    A.remove(j)
                    break
            else:
                C.append(A.pop(0))
        return C


print(Solution().advantageCount([2,7,11,15],[1,10,4,11]))
