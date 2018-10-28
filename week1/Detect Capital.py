class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        all_caps=False
        if(len(word)<=1):
            return True
        if(word[:2].isupper()):
            all_caps=True
        for i in range(1,len(word)):
            if((all_caps and not word[i].isupper()) or ( not all_caps and  word[i].isupper())):
                return False
        return True
