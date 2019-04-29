# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        nodelist = set()
        currentnode = head
        while currentnode is not None:
            if currentnode not in nodelist:
                nodelist.add(currentnode)
                currentnode = currentnode.next
            else:
                return True
        return False

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        p1, p2 = head, head
        while(p2.next and p2):
            p1, p2 = p1.next, p2.next.next
            if p1 == p2:
                return True
        return False