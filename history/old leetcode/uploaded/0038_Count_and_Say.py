# 38. Count and Say

def next_num(string):
    out = ''
    index  = 0
    while index < len(string):
        step = 1       
        if index == len(string)-1:
            out += str(step)+string[index]
            break
        else:
            while index+step < len(string):      
                if string[index+step] == string[index]:
                    step += 1
                else: 
                    break
            out += str(step)+string[index]
        index += step
    return out

class Solution:
    def countAndSay(self, n: int) -> str:
        now = '1'
        if n == 1:
            return now
        for i in range(n-1):
            now = next_num(now)
        return now



        
        
        
        
        
        