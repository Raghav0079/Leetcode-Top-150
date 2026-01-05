'''
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.
'''
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        from collections import defaultdict, deque
        
        adj = defaultdict(list)
        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append((b, values[i]))
            adj[b].append((a, 1/values[i]))
            
        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1.0
            q, visit = deque(), set()
            q.append((src, 1.0))
            visit.add(src)
            while q:
                n, w = q.popleft()
                if n == target:
                    return w
                for nei, weight in adj[n]:
                    if nei not in visit:
                        q.append((nei, w * weight))
                        visit.add(nei)
                        
                    
            return -1.0
        return [bfs(q[0], q[1]) for q in queries]