class Solution:
    def findTheDifference(self, s, t):
        s_counter=collections.Counter(s)
        t_counter=collections.Counter(t)
        for ch in t_counter-s_counter:
            return ch

        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
