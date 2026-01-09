"""
Docstring for 433

A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.
"""



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
    
# Example test case
# startGene = "AACCGGTT"
# endGene = "AAACGGTA"
# bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
# sol = Solution()
# print(sol.minMutation(startGene, endGene, bank))  # Output: 2


