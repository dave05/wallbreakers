class Solution:
    def isPalindrome(self, s):
        clear_s=""
        for ch in s:
            if ch.isalpha() or ch.isdigit():
                clear_s+=ch
        for i in range(len(clear_s)//2):
            print(clear_s[i])
            if(clear_s[i].lower()!=clear_s[len(clear_s)-1-i].lower()):
                print(clear_s[i])
                return False
        return True
        """
        :type s: str
        :rtype: bool
        """
