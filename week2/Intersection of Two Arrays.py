class Solution:
    def intersection(self, nums1, nums2):
        intersection=[]
        for i in nums1:
            if i in nums2 and i not in intersection:
                intersection.append(i)
        return intersection
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
