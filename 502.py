import heapq

class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):

        projects = sorted(zip(capital, profits))
        maxProfitHeap = []
        n = len(projects)
        projectIdx = 0

        for _ in range(k):

            while projectIdx < n and projects[projectIdx][0] <= w:

                heapq.heappush(maxProfitHeap, -projects[projectIdx][1])
                projectIdx += 1


            if not maxProfitHeap:
                break


            w += -heapq.heappop(maxProfitHeap)
            
        return w
