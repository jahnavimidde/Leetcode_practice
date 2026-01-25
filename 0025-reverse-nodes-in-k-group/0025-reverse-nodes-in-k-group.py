# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or k==1:
            return head
        dummy=ListNode(0)
        dummy.next=head
        prev_tail=dummy
        new_head=head
        while new_head :
            Node=new_head
            temp =Node
            count=1
            while temp.next and count<k:
                count+=1
                temp=temp.next
            if count<k:
                break
            new_head=temp.next
            temp.next=None
            reversed_head=self.reverseList(Node)
            prev_tail.next=reversed_head
            Node.next=new_head
            prev_tail=Node
        
        return dummy.next
        
        


    def reverseList(self, head):
        prev =None 
        current=head
        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        return prev
    