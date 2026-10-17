class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        count=1
        maxi=1
        nums=sorted(nums)
        n=len(nums)
        if not nums:
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

        


        