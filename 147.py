# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def insertionSortList2(self, head):
        current = head
        while current is not None:
            if current is head:
                last = current
                current = current.next
            else:
                if current.val >= last.val:
                    last = current
                    current = current.next
                    continue
                last.next = current.next
                prev = head
                last2 = None
                while(prev is not last.next):
                    if prev is head and prev.val >= current.val:
                        current.next = prev
                        head = current
                        break
                    elif prev.val >= current.val:
                        last2.next = current
                        current.next = prev
                        break
                    else:
                        last2 = prev
                        prev = prev.next
                current = last.next
        return head



