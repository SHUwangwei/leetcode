# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements2(self, head, val):
        while head is not None and head.val == val:
            head = head.next

        current = head
        while current is not None and current.next is None:
            last = current.next
            while last is not None and last.val == val:
                last = last.next
            current.next = last
            current = last
        return head

    def removeElements(self, head, val):
        if not head:
            return None
        
        current = head
        
        while current.next:
            
            if current.next.val == val:
                current.next = current.next.next
            
            else:
                current = current.next
                
        return head.next if head.val == val else head