"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.
"""
class Solution(object):
    def insert(self, intervals, newinterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals:
            return [newinterval]
        
        result = []
        
        for i in range(len(intervals)):
            if newinterval [1]< intervals [i][0]:
                result.append(newinterval)
                return result + intervals[i:]
            elif newinterval [0]> intervals [i][1]:
                result.append(intervals[i])
            else:
                newinterval [0] = min(newinterval [0], intervals [i][0])
                newinterval [1] = max(newinterval [1], intervals [i][1])
        result.append(newinterval)
        return result
    
            
            
            
