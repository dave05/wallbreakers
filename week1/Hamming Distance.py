'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
'''
class Solution:
    def hammingDistance(self, x, y):
        get_bin= lambda x,n: format(x,'b').zfill(n)
        bin_x=get_bin(x,32)
        bin_y=get_bin(y,32)
        hamming_count=0
        for i in range(len(bin_y)):
            if(bin_x[i]!=bin_y[i]):
                hamming_count+=1
        return hamming_count
        """
        :type x: int
        :type y: int
        :rtype: int
        """
