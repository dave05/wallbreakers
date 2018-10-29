'''
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums =
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: nums =
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
'''
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
