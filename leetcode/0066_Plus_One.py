# 66. Plus One

class Solution:
    
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ''
        for num in digits:
            string += str(num)
        new = str(int(string) + 1)
        out = []
        for char in new:
            out.append(int(char))
        return out
    
    # def plusOne(self, digits: List[int]) -> List[int]:
    #     end = -1
    #     digits[end] += 1
    #     while digits[end] > 9:
    #         digits[end] = 0
    #         end -= 1
    #         if -end > len(digits):
    #             break
    #         else:
    #             digits[end] += 1 
    #     if digits[0] == 0:
    #         digits.insert(0,1)
    #     return digits
        
        