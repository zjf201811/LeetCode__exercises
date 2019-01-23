class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        min_len = min([len(x) for x in strs])
        strs_len = len(strs)
        if strs==[]:
            return ""
        n = 0
        while n < min_len:
            for i in range(strs_len-1):
                if strs[i][n] != strs[i+1][n]:
                    return strs[0][0:n]
            else:
                n += 1
        return strs[0][0:n]
print(Solution().longestCommonPrefix(["f","flow","flight"]))