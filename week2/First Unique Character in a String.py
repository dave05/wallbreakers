'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''

class Solution:
    def firstUniqChar(self, s):
        seen_before=[]
        for i in range(len(s)):
            if s[i] not in s[i+1:] and s[i] not in seen_before:
                return i
            seen_before.append(s[i])
        return -1
        """
        :type s: str
        :rtype: int
        """
