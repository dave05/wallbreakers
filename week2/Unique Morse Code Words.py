class Solution:
    def uniqueMorseRepresentations(self, words):
        moore_code=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        moore_code_dict=dict()
        for word in words:
            code=""
            for ch in word:
                code+=moore_code[ord(ch)-ord('a')]
            moore_code_dict[word]=code
        distnict_codes=set(moore_code_dict.values())
        return len(distnict_codes)
        """
        :type words: List[str]
        :rtype: int
        """
