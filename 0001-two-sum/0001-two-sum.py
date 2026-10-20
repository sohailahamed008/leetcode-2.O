class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d={}
        n=len(nums)
        for i in range(n):
            a=target-nums[i]
            if a in d:
                return [d[a],i]
            else:
                d[nums[i]]=i

        

        

        
        