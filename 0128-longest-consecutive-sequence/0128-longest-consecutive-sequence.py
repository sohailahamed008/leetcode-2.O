class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        a=set(nums)
        n=len(nums)
        count=1
        maxi=0
        for i in a:
            if i-1 not in a:
                count=1
                while i+count in a:
                    count+=1
                maxi=max(maxi,count)
        return maxi    

        


        