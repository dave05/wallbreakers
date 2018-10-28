class Solution:
    def reverseString(self, s):
        d=''
        for i in range(len(s)-1,-1,-1):
            d+=s[i]
        return d
        """
        :type s: str
        :rtype: str
        """
        
