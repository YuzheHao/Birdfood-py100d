# 35. Search Insert Position

class Solution:
    
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target: return i
        return len(nums)
    
    # def searchInsert(self, nums: List[int], target: int) -> int:
    #     index = 0
    #     for n in nums:
    #         if n >= target: return index
    #         index += 1
    #     return len(nums)
        
    
    # def searchInsert(self, nums: List[int], target: int) -> int:
    #     if target in nums: 
    #         return nums.index(target)
    #     else:
    #         nums.append(target)
    #         nums.sort()
    #         return nums.index(target)