class Solution:
    def uncommonFromSentences(self, A, B):
        words_dict=dict()
        for word in A.split(" "):
            words_dict[word]=words_dict.get(word,0)+1
            #print(word)
        for word in B.split(" "):
            words_dict[word]=words_dict.get(word,0)+1
        uncommon_words=[]
        for key,value in words_dict.items():
            if value==1:
                uncommon_words.append(key)
        return uncommon_words
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        
