# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        if not head.next:
            return head
        prev=head
        curr=head.next
        while curr:
            if  curr.val==prev.val:
                prev.next=curr.next
                
                curr=curr.next
            else:
                prev=prev.next
                curr=curr.next
            
        return head