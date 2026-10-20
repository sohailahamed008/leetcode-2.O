class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n=len(nums)
        p=[1]*n
        lp=1
        for i in range(n):
            p[i]=lp*p[i]
            lp=lp*nums[i]
        rp=1
        for i in range(n-1,-1,-1):
            p[i]=rp*p[i]
            rp=rp*nums[i]

        return p


            
            
            