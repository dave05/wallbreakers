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
