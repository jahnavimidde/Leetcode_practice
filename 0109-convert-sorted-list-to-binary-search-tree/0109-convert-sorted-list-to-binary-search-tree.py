class Solution:
    def sortedListToBST(self, head):
        if not head:
            return None

        
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        
        if prev:
            prev.next = None
        else:
            head = None

        root = TreeNode(slow.val)

        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)

        return root