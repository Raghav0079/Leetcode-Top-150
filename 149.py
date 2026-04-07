import collections
import fractions 

class Solution(object):
    def maxPoints(self, points):
        n = len(points)
        if n <= 2: return n
        res = 1
        for i in range(n):
            count = collections.defaultdict(int)
            p1 = points[i]
            for j in range(i + 1, n):
                p2 = points[j]
                dx = p2[0] - p1[0]
                dy = p2[1] - p1[1]
                
      
                g = fractions.gcd(dx, dy)
                
                slope = (dx // g, dy // g)
                count[slope] += 1
                res = max(res, count[slope] + 1)
        return res
