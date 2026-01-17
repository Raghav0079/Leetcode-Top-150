"""Given the head of a linked list,
return the list after sorting it in ascending order."""

# define solution class
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # base case
        if not head or not head.next:
            return head

        # Split the linked list into two halves
        mid = self.getMid(head)
        right = mid.next
        mid.next = None
        left = head

        # Recursively sort both halves
        left = self.sortList(left)
        right = self.sortList(right)

        return self.merge(left, right)
# helper function to get the middle of the linked list
    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
# helper function to merge two sorted linked lists
    def merge(self, left, right):
        dummy = ListNode(0)
        tail = dummy
        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        if left:
            tail.next = left
        if right:
            tail.next = right
        return dummy.next
