# 88. Merge Sorted Array

class Solution:
    # def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    #     """
    #     Do not return anything, modify nums1 in-place instead.
    #     """
    #     for i in range(n):
    #         nums1.pop(-1)
    #     for v in nums2:
    #         nums1.append(v)
    #     nums1.sort()
    #     return nums1
    
    
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1,p2=0,0
        temp=nums1.copy() #copied num1 to temp
        nums1.clear() #make num1 as empty list
        while(p1<m and p2<n):
            if (temp[p1]<nums2[p2]):
                nums1.append(temp[p1])
                p1+=1
            else:
                nums1.append(nums2[p2]) 
                p2+=1
        while(p1<m):
            nums1.append(temp[p1])
            p1+=1
        while(p2<n):
            nums1.append(nums2[p2])
            p2+=1