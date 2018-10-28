class Solution:
    def reverse_aword(self,word):
        w=""
        for i in range(len(word)-1,-1,-1):
            w+=word[i]
        return w
    def reverseWords(self, s):
        reverse_s=""
        for word in s.split(" "):
            reverse_s+=self.reverse_aword(word)+ " "
        return reverse_s.strip()


        """
        :type s: str
        :rtype: str
        """
        
