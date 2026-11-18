class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(intervals)-1):
            for j in range(len(intervals)-1-i):
                if intervals[j][0]>intervals[j+1][0]:
                    intervals[j],intervals[j+1] = intervals[j+1],intervals[j]

        i = 0
        while i < len(intervals) - 1:
            if intervals[i][1] >= intervals[i+1][0]:
                if intervals[i][1] < intervals[i+1][1]:
                    intervals[i][1] = intervals[i+1][1]
                intervals.remove(intervals[i+1])
            else:
                i += 1

        return intervals