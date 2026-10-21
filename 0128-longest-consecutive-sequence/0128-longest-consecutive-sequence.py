class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums.sort()
        count=1
        maxi=1
        n=len(nums)
        if n==0:
            return 0
        for i in range(1,n):
            if nums[i]==nums[i-1]:
                continue
            if nums[i]==nums[i-1]+1:
                count+=1
                
            else:
                count=1
            maxi=max(maxi,count)
        return maxi
        