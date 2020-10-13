# 83. Remove Duplicates from Sorted List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        prev = head
        now = head.next
        while now != None:
            if now.val == prev.val:
                prev.next = now.next
                now = now.next
            else:
                prev = now
                now = now.next
        return head