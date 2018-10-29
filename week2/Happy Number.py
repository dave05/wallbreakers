'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example:

Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

'''

class Solution:
    def isHappyRec(self,memo,n):
        if n==1:
            return True
        if n in memo:
            return False
        memo.append(n)
        new_num=0
        while n>0:
            new_num+=pow(int(n%10),2)
            #print(int(n%10))
            n/=10
        #print(new_num)
        return self.isHappyRec(memo,new_num)
    def isHappy(self, n):
        memo=[]
        #new_num=0
        return self.isHappyRec(memo,n)

        """
        :type n: int
        :rtype: bool
        """
