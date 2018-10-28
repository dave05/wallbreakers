class Solution:
    def findComplement(self, num):
        bin_num=bin(num)
        inv=''
        for i in range(2,len(bin_num)):
            if bin_num[i]=='0':
                inv+='1'
            else:
                inv+='0'
        inv_num=int(inv,2)
        print(inv,bin_num)
        return inv_num
        """
        :type num: int
        :rtype: int
        """
        
