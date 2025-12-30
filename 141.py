'''Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

'''

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        return False
    
        
    
# time complexity: O(n)
# space complexity: O(1)
# n is the number of nodes in the linked list
# Floyd's Tortoise and Hare algorithm
# two pointers technique
# slow pointer moves one step at a time
# fast pointer moves two steps at a time
# if there is a cycle, they will meet at some point
