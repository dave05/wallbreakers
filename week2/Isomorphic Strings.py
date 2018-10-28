class Solution:
    def isIsomorphic(self, s, t):
        if len(s)!=len(t):
            return False
        replacements=dict()
        for i in range(len(s)):
            if s[i] not in replacements:
                if t[i] in replacements.values():
                    return False
                replacements[s[i]]=t[i]
            elif replacements[s[i]]!=t[i]:
                return False
        return True

        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
