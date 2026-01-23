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
        
        arr1, arr2 = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(arr1) < len(arr2):
            arr1, arr2 = arr2, arr1

        l, r = 0, len(arr1) - 1
        while True:
            i = (l + r) // 2  # arr1
            j = half - i - 2  # arr2

            Aleft = arr1[i] if i >= 0 else float("-infinity")
            Bleft = arr2[j] if j >= 0 else float("-infinity")
            Aright = arr1[i + 1] if (i + 1) < len(arr1) else float("infinity")
            Bright = arr2[j + 1] if (j + 1) < len(arr2) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)

                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
