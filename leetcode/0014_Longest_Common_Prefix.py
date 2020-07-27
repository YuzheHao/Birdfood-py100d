# 0014_Longest_Common_Prefix

class Solution:
    # 最简单粗暴的一个一个对比
    def longestCommonPrefix_0(self, strs: List[str]) -> str:
        ans = ''
        
        # empty input case:
        if len(strs) == 0: return ans
        
        # single input case:
        elif len(strs) ==1: return strs[0]
        
        
                # empty input case:
        if len(strs) == 0: return ans
        
        # single input case:
        elif len(strs) ==1: return strs[0]
        
        # normal case:
        else:
            for i in range(len(strs[0])):
                flag = 0 
                for str in strs[1:]:
                    # if compared string is shorter than current position
                    # OR: characters not matched
                    if len(str)<i+1 or str[i]!=strs[0][i]:
                        flag = 1
                        break
                if flag == 0:
                    ans += strs[0][i]
                else:
                    break
            return ans
        
        
#         # normal case (by using while()):
#         else:
#             for i in range(len(strs[0])):
#                 current = 1
#                 MATCHED = True
#                 while(current<=len(strs)-1):
#                     # if compared string is shorter than current position
#                     # OR: characters not matched, then break
#                     if len(strs[current])<i+1 or strs[current][i]!=strs[0][i]:
#                         MATCHED = False
#                         break
#                     current += 1
#                 if MATCHED:   
#                     ans += strs[0][i]
#                 else:
#                     break
#             return ans

    # python有太多方便的用法了……像这个min，就可以直接把数组里最短长度的元素找出来了
    # 然后下面这个all的用法，我一开始也想到了，但是语法不会用
    # 思路和我是一样的
    def longestCommonPrefix_1(self, strs):
        prefix=""
        if len(strs)==0: return prefix
        for i in range(len(min(strs))):
            c=strs[0][i]
            if all(a[i]==c for a in strs):
                prefix+=c
            else:
                break
        return prefix
    
    
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        if len(strs) == 1: return strs[0]
        
        strs.sort() # string的sorting居然是根据元素的长度排序，有点神奇
        p = ""
        # 我去zip这个函数简直就是为了这种情况量身定做的啊
        # 这种只对比最长和最短的两个的手法简直神来之笔啊，太厉害了
        for x, y in zip(strs[0], strs[-1]):
            if x == y: p+=x
            else: break
        return p
            
        

        
        
        

        