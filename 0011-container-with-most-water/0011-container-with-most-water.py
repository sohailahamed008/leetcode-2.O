class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxi=0
        n=len(height)
        i=0
        j=n-1
        while i<j:
            length=j-i
            h=min(height[i],height[j])
            area=length*h
            maxi=max(area,maxi)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1

        return maxi

        