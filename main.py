class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        le = min(strs, key=len)
        result = ''
        count = 0
        paletter = True
        for p in range(len(le)):
            container = ''
            if paletter == True:
                for i in range(len(strs)):
                    if strs[i][p] == le[p]:
                        if le[p] not in container:
                            container += le[p]
                    else:
                        paletter = False
                        # container = ''
                        # break
                        return result
                result += container
        return result
