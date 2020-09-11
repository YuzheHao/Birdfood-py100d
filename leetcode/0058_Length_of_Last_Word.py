# 58. Length of Last Word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        end = -1
        new = s.split(' ')
        while len(new[end]) == 0 and end != -len(new):
            end -= 1
        return len(new[end])