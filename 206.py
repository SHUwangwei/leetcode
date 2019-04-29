# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList2(self, head):
        l = head
        count = 0
        nodelist = []
        while l is not None:
            nodelist.append(l)
            count += 1
            l = l.next
        if len(nodelist) == 0:
            return None
        newhead = nodelist.pop()
        newhead2 = newhead
        print(newhead.val)
        for node in reversed(nodelist):
            newhead2.next = node
            newhead2 = node
        newhead2.next = None
        return newhead

    def reverseList(self, head):

        prev = None

        while head is not None:
            temp = head.next

            head.next = prev

            prev = head

            head = temp

        return prev
