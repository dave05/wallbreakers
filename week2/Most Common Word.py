class Solution:
    def mostCommonWord(self, paragraph, banned):
        word_counter=collections.Counter([word.lower() for word in re.findall(r'\w+',paragraph)])
        most_common_words=word_counter.most_common(len(banned)+1)
        for word_set in most_common_words:
            if word_set[0].lower() not in banned:
                return word_set[0].lower()
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
