# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0)
        dummy.next=head
        slow=dummy
        fast=dummy
        for i in range(n):
            fast=fast.next
        while fast and fast.next:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return dummy.next


        