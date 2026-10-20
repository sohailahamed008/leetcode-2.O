class Solution:
    def trap(self, height: list[int]) -> int:
        lh=[]
        n=len(height)
        maxl=height[0]
        for i in range(n):
            if height[i]>maxl:
                maxl=height[i]
            lh.append(maxl)
        rh=[]    
        maxh=height[-1]
        for i in range(n-1,-1,-1):
            if height[i]>maxh:
                maxh=height[i]
            rh.append(maxh)
        result=0
        rh.reverse()
        for i in range(n):
            mini=min(lh[i],rh[i])
            w=mini-height[i]
            result+=w

        return result
            
        
                    