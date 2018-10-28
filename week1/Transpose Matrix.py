class Solution:
    def transpose(self, A):
        L=[[0 for i in range(len(A))] for j in range(len(A[0]))]
        for row in range(len(A)):
            for col in range(len(A[0])):
                L[col][row]=A[row][col];
        return L
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
