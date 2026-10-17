class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n=len(nums)
        a=[1]*n
        lp=1
        for i in range(0,n):
            a[i]=a[i]*lp
            lp=lp*nums[i]
        rp=1
        for i in range(n-1,-1,-1):
            a[i]=a[i]*rp
            rp=rp*nums[i]
        return a
            
            
            