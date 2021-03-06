'''
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.
Example 1:
Input:s1 = "ab" s2 = "eidbaooo"
Output:True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False
Note:
The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
'''

class Solution:
    def checkInclusion(self, s1, s2):
        if not s1:
            return True
        if len(s2)<len(s1):
            return False
        s1_counter=collections.Counter(s1)
        s2_counter=collections.Counter(s2[:len(s1)])
        if s1_counter==s2_counter:
            return True
        for i in range(1,len(s2)-len(s1)+1):
            s2_counter.update(s2[i+len(s1)-1])
            s2_counter-=collections.Counter(s2[i-1])
            if s1_counter==s2_counter:
                return True
        return False
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
