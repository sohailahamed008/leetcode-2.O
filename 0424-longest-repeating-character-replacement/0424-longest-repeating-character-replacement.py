class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d={}
        l=0
        maxi=0
        res=0
        n=len(s)
        for r in range(n):
            if s[r] in d:
                d[s[r]]+=1
            
            else:
                d[s[r]]=1
            maxi=max(d[s[r]],maxi)
            while r-l+1-maxi>k:
                d[s[l]]-=1
                l+=1
            res=max(r-l+1,res)
        return res



        

        