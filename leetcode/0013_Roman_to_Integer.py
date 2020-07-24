# 0013_Roman_to_Integer
class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {'I':1,
                'V':5,
                'X':10,
                'L':50,
                'C':100,
                'D':500,
                'M':1000}
        sum = 0
        previous = 0
        for char in s:
            now = dict[char]
            if now <= previous:
                sum += now
            else:
                sum += (now-2*previous)
            previous = now
        return sum
    
    
# 像这种需要对比序列内元素前后关系的情况下，用range来循环会更好一点，因为这样的话，在每一次循环中，序列中的每个元素都是可以被调用的
# 相比我上一种做法，我不需要专门把之前的数字储存起来用作下一次循环的对比，而且也不需要，用减去两倍的先前值这样的操作来抵消之前的误操作，科学多了
    def romanToInt_0(self, s: str) -> int:
        romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i in range(len(s)-1):
            if romans[s[i]]  < romans[s[i+1]]:
                res -= romans[s[i]]
            else:
                res += romans[s[i]]
                
        res += romans[s[len(s)-1]