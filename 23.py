"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        # base case 
        if not lists or len(lists) == 0:
            return None
        # iterative while loop until we have only one list
        while len(lists) > 1:
            mergedList =[]
            # loop through pairs of lists
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists [i+1] if (i+1) < len(lists) else None 
                mergedList.append(self.mergeList(l1,l2))
            lists = mergedList
        return lists[0]
    
    # function for merging the lists     
    def mergeList(self,L1,L2):
        dummy=ListNode(0)
        tail = dummy
        # while loop on L! and L2
        while L1 and L2 :
            if L1.val < L2.val :
                tail.next = L1
                L1 = L1.next
            else :
                tail.next = L2 
                L2 = L2.next
            tail = tail.next
            # attaching the remaining nodes
        if L1 :
            tail.next = L1
        if L2 : 
            tail.next = L2
        return dummy.next

# Explanation:
# We use a divide and conquer approach to merge k sorted linked lists. In each iteration,
# we merge pairs of linked lists until only one linked list remains. The mergeList function merges two sorted linked lists into one sorted linked list. We use a dummy node to simplify the merging process. The overall


          

                
                
# time complexity is O(N log k) where N is the total number of nodes and k is the number of linked lists.
# space complexity is O(1) as we are not using any extra space for merging the lists.

