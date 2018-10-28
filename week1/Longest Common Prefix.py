class Solution:
    def longest_prefix_forTwo(self,s1,s2):
        result=''
        short_len = len(s1) if len(s1)<=len(s2) else len(s2)
        for i in range(short_len):
            if s1[i]!=s2[i]:
                break
            result+=s1[i]
        return result
    def longestCommonPrefix(self, strs):
        if len(strs)==0:
            return''
        if len(strs)==1:
            return strs[0]
        match=self.longest_prefix_forTwo(strs[0],strs[1])
        for i in range(2,len(strs)):
            if len(match)==0:
                break
            match=self.longest_prefix_forTwo(match,strs[i])
        return match

        """
        :type strs: List[str]
        :rtype: str
        """
        
