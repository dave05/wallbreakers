class Solution:
    def selfDividingNumbers(self, left, right):
        if right<10:
            return [i for i in range(left,right+1)]
        l=[]
        for i in range(left,right+1):
            if(i<10):
                l.append(i)
                continue
            num=i
            l.append(i)
            while(num//10!=0):
                digit=num%10
                if(digit==0):
                    l.pop()
                    break
                if(i%digit!=0):
                    l.pop()
                    break
                num=num//10
            if(i%num!=0 and i in l):
                l.pop()
        return l
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
