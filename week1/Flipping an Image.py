class Solution:
    def flipAndInvertImage(self, A):
        for i in range(len(A)):
            A[i].reverse()
            for j in range(len(A[0])):
                A[i][j]=int(not A[i][j])

            '''if A[i][j]==0:
                    A[i][j]=1
                else:
                    A[i][j]=0'''
        return A
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
