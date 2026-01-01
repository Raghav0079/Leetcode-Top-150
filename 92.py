'''Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.'''


class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0,head)
        
        # 1. reach node at position left
        leftprev,cur=dummy,head
        for i in range(left-1):
            leftprev,cur=cur,cur.next
            
        # 2. reverse from left to right
        prev=None
        for i in range(right-left+1):
            tmpnxt=cur.next
            cur.next=prev
            prev,cur=cur,tmpnxt
            
        # 3. reconnect the reversed part
        leftprev.next.next=cur
        leftprev.next=prev
        
        return dummy.next
    
        
            