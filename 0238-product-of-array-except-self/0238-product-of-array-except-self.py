class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n=len(nums)
        answer=[1]*n
        left_pro=1
        for i in range(n):
            answer[i]=left_pro
            left_pro*=nums[i]
        right_pro=1
        for i in range(n-1,-1,-1):
            answer[i]*=right_pro
            right_pro*=nums[i]
        return answer
            
            