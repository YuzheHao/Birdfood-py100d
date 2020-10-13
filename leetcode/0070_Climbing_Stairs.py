# 70. Climbing Stairs

class Solution:

#     def climbStairs(self, n: int) -> int:
#         def A(n):
#             res = 1
#             for i in range(1,n+1):
#                 res *= i
#             return res

#         ways = 0
#         for x in range(n+1):
#             if (n-x) % 2 == 0:
#                 y = int((n-x) / 2) 
#                 ways += A(x+y)/(A(x)*A(y))
                    
#         return int(ways)

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        from_1, from_2 = 1, 1
        for i in range(n-1):
            from_1, from_2 = from_2, from_2+from_1
        return from_2