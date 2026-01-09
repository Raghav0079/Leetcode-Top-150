class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        # BFS
        from queue import Queue
        bank  = set(bank)
        if end not in bank:
            return -1
        # BFS
        queue = Queue()
        queue.put((start, 0))
        visited = {start}
        # BFS
        while not queue.empty(): # while queue is not empty
            gene,level = queue.get()
            # Check if we reached the end gene
            if gene == end:
                return level
            # Try all possible mutations
            for i in range(len(gene)):
                for c in 'ACGT':  # possible gene characters
                    new_gene =gene  [:i] + c + gene[i+1:]
                    queue.put((new_gene, level + 1))
                    visited.add(new_gene)
        return -1
# time complexity: O(N * M) where N is the number of genes in the bank and M is the length of each gene
# space complexity: O(N)
    
