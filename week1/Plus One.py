class Solution:
    def plusOne(self, digits):
        sum=[0]+digits
        carry=1
        for i in range(len(digits)-1,-1,-1):
            digit_sum=digits[i]+carry
            if(digit_sum<10):
                sum[i+1]=digit_sum
                carry=0
                break
            carry=digit_sum//10
            digit_sum=digit_sum%10
            sum[i+1]=digit_sum
        if(carry==0):
            sum.pop(0)
        else:
            sum[0]=carry
        return sum
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
