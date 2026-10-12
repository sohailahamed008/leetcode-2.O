class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n=len(nums)
        hash={}
        for i in range(0,n):
            rem=target-nums[i]
            if rem in hash:
                return [hash[rem],i]
            else:
                hash[nums[i]]=i

        

        
        