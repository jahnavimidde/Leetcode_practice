# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        d1=headA
        d2=headB
        while d1!=d2:
            d1=headB if d1==None else d1.next
            d2=headA if d2==None else d2.next
        return d1
        
        