class Solution:
    def partition(self, head, x):
        small = small_head = ListNode(0)
        large = large_head = ListNode(0)

        curr = head

        while curr:
            if curr.val < x:
                small.next = curr
                small = small.next
            else:
                large.next = curr
                large = large.next

            curr = curr.next

        large.next = None
        small.next = large_head.next

        return small_head.next