# 69. Sqrt(x)

class Solution:
    
    # def mySqrt(self, x: int) -> int:
    #     return int(sqrt(x))
    
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        down = 0
        up = x
        now = x // 2
        while up != down+1:
            while now*now > x:
                up = now
                now = down + (now-down) // 2
            down = now
            now = up
        return down
        
            