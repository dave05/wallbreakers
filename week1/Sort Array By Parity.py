class Solution:
    def sortArrayByParity(self, A):
        return [i for i in A if i%2==0] + [i for i in A if i%2!=0]
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
