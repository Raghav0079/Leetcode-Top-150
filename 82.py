'''Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        
        dummyNode=ListNode(0)
        dummyNode.next=head
        prev=dummyNode
        curr=head

        while curr!=None and curr.next!=None:

            if curr.next!=None and curr.val==curr.next.val:

                while curr.next!=None and curr.val==curr.next.val:

                    curr=curr.next

                prev.next=curr.next

            else:

                prev=prev.next

            curr=curr.next

        return dummyNode.next

# time complexity: O(n)
# space complexity: O(1)        
