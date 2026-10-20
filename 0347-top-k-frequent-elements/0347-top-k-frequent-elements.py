class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        s=sorted(d,key=d.get,reverse=True)
        return s[:k]

        


            
        