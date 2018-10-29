'''
We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words.

You may return the list in any order.



Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: A = "apple apple", B = "banana"
Output: ["banana"]


Note:

0 <= A.length <= 200
0 <= B.length <= 200
A and B both contain only spaces and lowercase letters.

'''
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
