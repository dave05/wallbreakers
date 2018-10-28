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
