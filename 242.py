''' Given two strings s and t, return true if t is an anagram of s, and false otherwise.'''

class Solution(object):
    def isAnagram(self,s,t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        
        for i in range(len(s)):
            countS[s[i]]=1+countS.get(s[i], 0)
            countT[t[i]]=1+countT.get(t[i], 0)
            
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True

# time complexity: O(n)
# space complexity: O(1) since the size of the hash maps will be at most 26 for lowercase letters

            
