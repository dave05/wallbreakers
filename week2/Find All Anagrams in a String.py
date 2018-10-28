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
        
