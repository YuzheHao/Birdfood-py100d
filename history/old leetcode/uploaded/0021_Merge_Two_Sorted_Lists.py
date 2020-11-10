# 21. Merge Two Sorted Lists

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    # def extract_val(nodelist):
    #     val_list = []
    #     while nodelist != None:
    #         val_list.insert(0,nodelist.val)
    #         nodelist = nodelist.next
    #     return val_list
    #
    # def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     l1v = extract_val(l1)
    #     l2v = extract_val(l2)
    #     newlist = l1v+l2v
    #     newlist.sort()
    #     newlist.reverse()
    #     result = None
    #     for v in newlist:
    #         result = ListNode(v,result)
    #     return result
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = []
        while(l1!=None and l2!=None):
            if l1.val <= l2.val:
                result.insert(0,l1.val)
                l1 = l1.next
            else:
                result.insert(0,l2.val)
                l2 = l2.next
                
        if l1 == None:
            while(l2!=None):
                result.insert(0,l2.val)
                l2 = l2.next
        elif l2 == None:
            while(l1!=None):
                result.insert(0,l1.val)
                l1 = l1.next
        
        out = None
        for v in result:
            out = ListNode(v,out)
        return out

