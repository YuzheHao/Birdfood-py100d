# 26. Remove Duplicates from Sorted Array

class Solution:
    
    # def removeDuplicates(self, nums: List[int]) -> int:
    #     for elem in nums:
    #         for i in range(nums.count(elem)-1):
    #             nums.remove(elem)
    #     return len(nums)
    
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i+1 < len(nums):
            while nums[i] == nums[i+1]:
                del nums[i+1]
                if i+1 >= len(nums): break
            i += 1
        return len(nums)
           