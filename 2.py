'''You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.'''

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        curr = dummy
        
        carry=0
        while l1 or l2 or carry  :
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # new digit 
            val = v1 + v2 + carry
            # 15
            carry = val // 10
            val = val % 10
            
            curr.next = ListNode(val)
            
            #update pointers
            curr = curr.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        
        # edge case 
        
        return dummy.next

# time complexity: O(max(m,n)) where m and n are the lengths of the two linked lists.
# space complexity: O(max(m,n)) for the new linked list.
