# 28. Implement strStr()

class Solution:
    
    # def strStr(self, haystack: str, needle: str) -> int:
    #     if len(needle) == 0 : return 0
    #     elif len(haystack)==0 or len(haystack)<len(needle): return -1
    #     elif len(needle) == len(haystack): 
    #         if needle == haystack: return 0
    #         else: return -1
    #     for i in range(len(haystack)-len(needle)+1):
    #         if haystack[i]==needle[0]:
    #             j = 1
    #             flag = 1
    #             while j<len(needle):
    #                 if haystack[i+j]!=needle[j]:
    #                     flag = 0
    #                     break
    #                 j += 1
    #             if flag == 1:
    #                 return i
    #     return -1
    
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == '' and needle != '':
            return -1
        if needle == '':
            return 0
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1
        