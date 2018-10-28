class Solution:
    def reverseVowels(self, s):
        list_vowels=['a','e','i','o','u']
        s_list=list(s)
        right=len(s_list)
        for i in range(len(s_list)):
            if(s_list[i].lower() in list_vowels):
                for j in range(right-1,i,-1):
                    if(s_list[j].lower() in list_vowels):
                        s_list[i],s_list[j]=s_list[j],s_list[i]
                        right=j
                        break
        vowel_swaped_s=''
        for ch in s_list:
            vowel_swaped_s+=ch
        return vowel_swaped_s
        """
        :type s: str
        :rtype: str
        """
