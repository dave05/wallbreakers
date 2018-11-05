'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.
'''

class Solution:
    def isAnagram(self, s, t):
        s_counter=collections.Counter(s)
        t_counter=collections.Counter(t)
        return s_counter==t_counter
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
