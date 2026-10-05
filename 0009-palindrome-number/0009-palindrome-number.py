class Solution:
    def isPalindrome(self, x: int) -> bool:
        n=x
        result=0
        if n<0:
            return False
        while n>0:
            ld=n%10
            result=result*10+ld
            n=n//10
        return result==x
        