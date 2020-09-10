# 53. Maximum Subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum, min_so_far, max_sub = 0, 0, float('-inf')
        for ele in nums:
            cur_sum += ele 
            max_sub, min_so_far= max(cur_sum - min_so_far, max_sub), min(min_so_far, cur_sum) 
        return max_sub

