class Solution:
    def findErrorNums(self, nums):
        nums_counter=collections.Counter(nums)
        duplicate=nums_counter.most_common(1)[0][0]
        skipped_num_counter=collections.Counter([i for i in range(len(nums)+1)])-nums_counter
        for key in skipped_num_counter:
            skipped_num=key
        return [duplicate,skipped_num]


        """
        :type nums: List[int]
        :rtype: List[int]
        """
