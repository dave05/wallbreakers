'''
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

'''

class Solution:
    def minDistance(self, word1, word2):
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        memo=dict()
        return self.minDistanceR(word1,len(word1)-1,word2,len(word2)-1,memo)
    def minDistanceR(self,w1,l1,w2,l2,memo):
        if (l1,l2) in memo :
            return memo[(l1,l2)]
        if l1<0:
            return (l2+1)
        if l2<0:
            return (l1+1)
        if w1[l1]==w2[l2]:
            memo[(l1,l2)]=self.minDistanceR(w1,l1-1,w2,l2-1,memo)
        else:
            memo[(l1,l2)]=min(self.minDistanceR(w1,l1,w2,l2-1,memo),self.minDistanceR(w1,l1-1,w2,l2,memo),self.minDistanceR(w1,l1-1,w2,l2-1,memo))+1
        return memo[(l1,l2)]


        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
