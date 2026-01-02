'''Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.'''

class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """     
        left,right = ListNode(0),ListNode(0)
        ltail,rtail = left,right
        
        while head:
            if head.val < x :
                ltail.next=head
                ltail=ltail.next
            else:
                rtail.next=head
                rtail=rtail.next
            head=head.next
        ltail.next=right.next
        rtail.next=None
        return left.next
    
# time complexity: O(n)
# space complexity: O(1)
