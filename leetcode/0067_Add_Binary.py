# 67. Add Binary

class Solution:
    
    # def addBinary(self, a: str, b: str) -> str:
    #     diff = len(a)-len(b)
    #     if diff > 0:
    #         unchanged = a[:diff]
    #         a = a[diff:]
    #     elif diff < 0:
    #         unchanged = b[:-diff]
    #         b = b[-diff:]
    #     else:
    #         unchanged = ''
    #     c = 0
    #     new = ''
    #     for i in range(1,len(a)+1):
    #         new_num = int(a[-i]) + int(b[-i]) + c
    #         c = new_num // 2
    #         new_num = new_num % 2
    #         new = str(new_num) + new
    #     for i in range(1,len(unchanged)+1):
    #         new_num = int(unchanged[-i]) + c
    #         c = new_num // 2
    #         new_num = new_num % 2
    #         new = str(new_num) + new
    #     if c != 0:
    #         new = '1' + new
    #     return new
    
    def addBinary(self, a: str, b: str) -> str:
        temp = bin(int(a,2) + int(b,2))
        # print(temp)
        return temp[temp.index("b")+1:]