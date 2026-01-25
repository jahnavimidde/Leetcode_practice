# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        if not head.next:
            return head
        mid=self.middle(head)
        left_head=head
        right_head=mid.next
        mid.next=None
        left=self.sortList(left_head)
        right=self.sortList(right_head)
        return self.merge_list(left,right)




    def middle(self,head):
            slow=head
            fast=head.next
            while fast and fast.next:
                fast=fast.next.next
                slow=slow.next
            return slow
    def merge_list(self,left,right):
            temp=ListNode(0)
            dummy=temp
            
            while (left != None and right != None):
                if left.val<right.val:
                    dummy.next=left
                    dummy=left
                    left=left.next
                else:
                    dummy.next=right
                    dummy=right
                    right=right.next
            if left:
                dummy.next=left
            if right:
                dummy.next=right
            return temp.next

                    
