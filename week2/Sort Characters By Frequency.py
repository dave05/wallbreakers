class Solution:
    def frequencySort(self, s):
        char_counter= collections.Counter(s)
        char_freq=char_counter.most_common()
        output=""
        for i in range(len(char_freq)):
            output+=(char_freq[i][0]*char_freq[i][1])
        return output
        """
        :type s: str
        :rtype: str
        """
        
