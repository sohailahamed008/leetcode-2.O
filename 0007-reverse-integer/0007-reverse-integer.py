class Solution:
    def reverse(self, x: int) -> int:
        num=x
        result=0
        if num<0:
            num=num*-1
        while num>0:
            ld=num%10
            result=(result*10)+ld
            num=num//10
        if x<0:
            return result*-1 if -(2**32)<=result<=(2**31-1) else 0
        return result if -(2**32)<=result<=(2**31-1) else 0

        