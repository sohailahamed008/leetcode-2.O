class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        maxi={}
        result=[]
        for i in nums:
            if i in maxi:
                maxi[i]=maxi[i]+1
            else:    
                maxi[i]=1
        sorted_maxi=sorted(maxi,key=maxi.get,reverse=True)
        return sorted_maxi[:k]
        


            
        