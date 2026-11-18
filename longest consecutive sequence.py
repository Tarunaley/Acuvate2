class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        count=1
        max_count=1
        result=[]
        n=len(nums)
        if n==0:
            return 0
        for i in range(n):
            for j in range(n-i-1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        for i in range(1,n):

            if nums[i]==nums[i-1]:
                continue
            elif nums[i]==nums[i-1]+1:
                count+=1
            else:
                count=1
            if count>max_count:
                max_count=count
        return(max_count)