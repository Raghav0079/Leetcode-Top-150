''' A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.'''


# intuition : filter out non-alphanumeric characters, convert to lowercase, and check if the string is equal to its reverse.
class Solution(object):
    def isPalindrome(self,s):
        """
        :type s: str
        :rtype: bool
        """
        # Filter out non-alphanumeric characters and convert to lowercase
        check = "".join([char.lower() for char in s if char.isalnum()])
        return check == check[::-1]   # Check if the string is equal to its reverse


# Time Complexity: O(n), where n is the length of the string s. We traverse the string once to filter and convert characters, and then again to check for palindrome.
# Space Complexity: O(n) for storing the filtered string.


# Example usage:
# sol = Solution()
# print(sol.isPalindrome("A man, a plan, a canal: Panama"))  # Output: True
# print(sol.isPalindrome("race a car"))  # Output: False    

