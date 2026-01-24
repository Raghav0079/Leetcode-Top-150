"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""

# defining the Solution class
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = []
        i,j = 0,0
        m,n = len(nums1),len(nums2)
        
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
                
        while i < m:
            merged.append(nums1[i])
            i += 1
            
        while j < n:
            merged.append(nums2[j])
            j += 1
            
        total = m + n
        mid = total // 2
        
        if total % 2 == 0:
            return (merged[mid - 1] + merged[mid]) / 2.0
        else:
            return merged[mid] * 1.0
        
        
