# 0020_Valid_Parentheses
# (Unfinished)
class Solution:
    def isValid(self, s: str) -> bool:
        dict = {
            '(':')',
            '[':']',
            '{':'}'
        }
        trans = {
            '(':0,')':0,
            '[':1,']':1,
            '{':2,'}':2
        }
        start = [0,0,0]
        for i in range(len(s)):
            if (s[i] in dict.keys()):
                
                if (dict[s[i]] in s[i:])
                
            