class Solution:
    def wordPattern(self, pattern, str):
        patternMap=dict()
        str_words=str.split(" ")
        if len(pattern)!=len(str_words):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in patternMap:
                if str_words[i] in patternMap.values():
                    return False
                patternMap[pattern[i]]=str_words[i]
            elif patternMap[pattern[i]]!=str_words[i]:
                return False
        return True

        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
