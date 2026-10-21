class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=i
        maxi=0
        count=0
        result=set()
        while j<len(s):
            if s[j] in result:
                result.clear()
                i+=1
                j=i
                count=0

            else:
                count+=1
                result.add(s[j])
                j+=1
                maxi=max(count,maxi)

        return maxi
            

        