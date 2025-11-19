'''Given an array of strings strs, group the anagrams together. You can return the answer in any order.'''

class Solution(object):
    def groupAnagrams(self,strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res= defaultdict(list) # mapping char count to list of anagrams
        
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')] +=1
                
            res[tuple(count)].append(s)
            
        return list(res.values())
                    
        
# time complexity: O(NK) where N is the number of strings and K is the maximum length of a string
# space complexity: O(NK) for the output list
