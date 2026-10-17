class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        d={}
        n=len(nums)
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        d=sorted(d,key=d.get,reverse=True)
        return d[0:k]
        


            
        