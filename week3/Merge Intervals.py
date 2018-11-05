'''
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.
'''

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        if not intervals:
            return intervals
        intervals.sort(key= lambda x:x.start)
        output=[]
        prev_end=intervals[0].end
        prev_begin=intervals[0].start
        for i in range(1,len(intervals)):
            if prev_end>=intervals[i].start:
                prev_end=max(prev_end,intervals[i].end)
                prev_begin=min(prev_begin,intervals[i].start)
            else:
                output.append(Interval(prev_begin,prev_end))
                prev_begin=intervals[i].start
                prev_end=intervals[i].end
        output.append(Interval(prev_begin,prev_end))
        return output
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        
