'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

'''

class Solution:
    def robRec(self,nums,index,memo):
        if index>=len(nums):
            return 0
        if memo[index]!=-1:
            return memo[index]
        if index==len(nums)-1:
            memo[index]=nums[index]
        if index==len(nums)-2:
            memo[index]=max(nums[index:])

        else:
            memo[index]=max(self.robRec(nums,index+2,memo)+nums[index],self.robRec(nums,index+1,memo))
        return memo[index]
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums)<=2:
            return max(nums)
        index=0
        memo1=[-1]*len(nums)
        memo2=[-1]*len(nums)
        return max(self.robRec(nums[:-1],index+2,memo1)+nums[index],self.robRec(nums,index+1,memo2))
        """
        :type nums: List[int]
        :rtype: int
        """
