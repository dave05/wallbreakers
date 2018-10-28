class Solution:
    def get_region_size(self,matrix,row,col,memo,min_value):
        if row<0 or row>=len(matrix) or col<0 or col>=len(matrix[0]):
            return 0
        if matrix[row][col]<=min_value:
            return 0
        if memo[row][col]!=-1:
            return memo[row][col]
        #visited[row][col]=True
        size=1
        min_value=matrix[row][col]
        for r in range(row-1,row+2):
            for c in range(col-1,col+2):
                if (c==col+1 and r==row+1) or (c==col-1 and r==row+1) or (c==col+1 and r==row-1) or (c==col-1 and r==row-1):
                    continue
                if r!=row or c!=col:
                    size=max(size,self.get_region_size(matrix,r,c,memo,min_value)+1)
                    #print(r,c,size)
        memo[row][col]=size
        return size
    def longestIncreasingPath(self, matrix):
        memo=[[-1 for i in range(len(matrix[0]))] for j in range(len(matrix)) ] # creating a memo table to keep track of what I already calculated
        longest=0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                size=self.get_region_size(matrix,row,col,memo,float("-inf")) # for the call set the minimum value as negative infinity.
                #print(row,col,size)
                longest=max(longest,size)
                '''else:
                    longest=visited[row][col]
                visited[row][col]=longest'''
        return longest
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
