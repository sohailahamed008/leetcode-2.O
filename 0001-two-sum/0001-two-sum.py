class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d1={}
        n=len(nums)
        for i in range(0,n):
            a=target-nums[i]
            if a in d1:
                return [d1[a],i]
            else:
                d1[nums[i]]=i
        

        

        
        