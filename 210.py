

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # build an adjacency list 
        prereq={ i: [] for i in range(numCourses)}
        
        for crs , pre in prerequisites:
            prereq[crs].append(pre)
            
        # a course has 3 possible states 
        # visited set : all nodes in the current path
        # visiting : crs not added to output but added in the cycle 
        # unvisited : crs not visited yet
        
        output=[]
        visit,cycle = set(), set()
        
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return output
    
        
            