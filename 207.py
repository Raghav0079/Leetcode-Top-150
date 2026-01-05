'''There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

'''
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        premap={i : [] for i in range(numCourses)}
        for crs,pre in prerequisites:
            premap[crs].append(pre)
            
        # visitSet = all nodes in the current path
        visitset=set()
        
        def dfs(crs):
            if crs in visitset:
                return False 
            if premap[crs]==[]:
                return True
            
            visitset.add(crs)
            for pre in premap[crs]:
                if not dfs(pre):
                    return False
            visitset.remove(crs)
            premap[crs]=[]
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
        