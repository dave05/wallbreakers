'''
A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
Note:

S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.
'''

class Solution:
    def partitionLabels(self, S):

        begin,end=0,0
        output=[]
        while begin<len(S):
            partition=''+S[begin]
            p_len=len(partition)
            i=0
            while i <p_len:
                end=max(end,S.rfind(partition[i]))
                if end!=-1:
                    partition=S[begin:end+1]
                p_len=len(partition)
                i+=1
            output.append(len(partition))
            begin=end+1
        return output

        """
        :type S: str
        :rtype: List[int]
        """
        
