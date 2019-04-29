# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode2(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        nodelistA = []
        nodelistB = []
        currentnode = headA
        while currentnode is not None:
            nodelistA.append(currentnode)
            currentnode = currentnode.next
        currentnode = headB
        while currentnode is not None:
            nodelistB.append(currentnode)
            currentnode = currentnode.next
        lengtha = len(nodelistA)
        lengthb = len(nodelistB)
        if lengtha == 0 or lengthb == 0:
            return None
        i = lengtha - 1
        j = lengthb - 1
        if nodelistA[i] != nodelistB[j]:
            return None
        while(i > -1 and j > -1):
            if nodelistA[i] == nodelistB[j]:
                i -= 1
                j -= 1
            else:
                return nodelistA[i + 1]
        if j == -1 or i == -1:
            if j == -1:
                return nodelistB[0]
            else:
                return nodelistA[0]
        else:
            return None

    def reverseList(self, head):

        prev = None

        while head is not None:
            temp = head.next

            head.next = prev

            prev = head

            head = temp

        return prev

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if (not headA) or (not headB):
            return None
        a, b = headA, headB
        while a != b:
            a = headB if a is None else a.next
            b = headA if b is None else b.next
        return a

