# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head :
            return
        if not  head.next :
            
            return head  
        length=1
        temp=head
        while temp.next:
            temp=temp.next
            length+=1


        k=k%length
        if k==0:
            return head


        slow=head
        fast=head

        
        while k:
            fast=fast.next
            k-=1
        
        while fast.next:
            slow=slow.next
            fast=fast.next
        some=slow.next
        slow.next=None
        fast.next=head
        return some


        
        