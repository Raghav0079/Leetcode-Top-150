class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        bank  = set(bank)
        if end not in bank:
            return -1
        
        queue = Queue()
        queue.put((start, 0))
        visited = {start}
        
        while not queue.empty():
            gene,level = queue.get()
            if gene == end:
                return level
            for i in range(len(gene)):
                for c in 'ACGT':
                    new_gene =gene  [:i] + letter + gene[i+1:]
                    queue.put((new_gene, level + 1))
                    visited.add(new_gene)
        return -1
    
    