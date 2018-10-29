'''
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''
class Solution:

    def findAnagrams(self, s, p):
        p_counter=collections.Counter(p) # create a counter for p
        output=[] # list of the starting indext of a substring in s which anagram with p.
        #sub_string=s[0:len(p)]
        prev=''
        sub_string_counter=collections.Counter(s[0:len(p)])
        if sub_string_counter-p_counter==p_counter-sub_string_counter:
                output.append(0)
        for i in range(len(p),len(s),1):
            sub_string_counter.update(s[i])
            prev=s[i-len(p)]
            sub_string_counter-=collections.Counter(prev)
            #print(p_counter)
            if sub_string_counter==p_counter:
                output.append(i-len(p)+1)

        return output
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
