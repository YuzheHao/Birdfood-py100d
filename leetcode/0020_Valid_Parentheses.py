# 0020.Valid Parentheses


class Solution:
    # with stack processing
    def isValid(self, s: str) -> bool:
        dict = {
            ')':'(',
            ']':'[',
            '}':'{',
            '(':None,
            '[':None,
            '{':None
        }
        stack = []
        for char in s:
            if len(stack)==0 or stack[0]!=dict[char]:
                stack.insert(0,char)
            else:
                del stack[0]
        if len(stack) == 0:
            return True
        else:
            return False
        
    ## with string processing    
    # def isValid(self, s):
    #     while "()" in s or "{}" in s or '[]' in s:
    #         s = s.replace("()", "").replace('{}', "").replace('[]', "")
    #     return s == ''
                
            