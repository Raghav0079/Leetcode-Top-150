'''Given the head of a linked list, remove the nth node from the end of the list and return its head.'''

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        while n > 0 and right :
            right = right.next
            n -= 1
            
        while right :
            left = left.next
            right = right.next
            
        # remove the nth node from end
        left.next = left.next.next
        return dummy.next

# time complexity: O(L) where L is the length of linked list
# space complexity: O(1)
