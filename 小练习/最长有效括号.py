# Author:ZJF
class Solution:
    def isValid(self, s):
        sdict={"]":"[","}":"{",")":"("}
        left=["{","[","("]
        slist=list(s)
        rlist=[]
        for i in slist:
            if i in left:
                rlist.append(i)
            elif not rlist or sdict[i] != rlist.pop(-1):
                return False


