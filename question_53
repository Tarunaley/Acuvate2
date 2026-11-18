class Solution(object):
    def maxSubArray( nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = float('-inf')
        total = 0

        for n in nums:
            total += n
            max_sum = max(max_sum, total)
            if total < 0:
                total = 0
        return max_sum