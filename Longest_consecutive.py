class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        s=set(nums)
        longest=0
        count=0
        for i in s:
            if i-1 not in s:
                count=1
                num=i
                while num+1 in s:
                    count+=1
                    num+=1
                longest=max(count,longest)
        return longest