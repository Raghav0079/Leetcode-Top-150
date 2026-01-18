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
        if L1 :
            tail.next = L1
        if L2 : 
            tail.next = L2
        return dummy.next
                
        
# example usage
# lists = [[1,4,5],[1,3,4],[2,6]]
# sol = Solution()
# merged_head = sol.mergeKLists(lists)
# while merged_head:
#     print(merged_head.val)
