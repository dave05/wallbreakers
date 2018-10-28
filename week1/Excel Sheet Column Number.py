class Solution:
    def code(self,ch):
        return ord(ch)-ord('A') +1
    def titleToNumber(self, s):

        col_num=0
        for i in range(len(s)):
            col_num+=self.code(s[i])*pow(26,len(s)-1-i)
        return col_num
        """
        :type s: str
        :rtype: int
        """
