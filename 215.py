import random

class Solution(object):
    def findKthLargest(self, nums, k):

        target = len(nums) - k
        
        def quickSelect(l, r):

            pivot_idx = random.randint(l, r)
            pivot = nums[pivot_idx]
            

            lt, i, gt = l, l, r
            
            while i <= gt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[gt], nums[i] = nums[i], nums[gt]
                    gt -= 1
                else:
                    i += 1
            

            
            if target < lt:
                return quickSelect(l, lt - 1)
            elif target > gt:
                return quickSelect(gt + 1, r)
            else:
                return nums[target]

        return quickSelect(0, len(nums) - 1)
