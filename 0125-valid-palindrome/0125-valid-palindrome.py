class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= "".join(s.lower() for s in s if s.isalnum())
        n=len(s)
        for i in range(n):
            if s[i] != s[n-i-1]:
                return False
        return True





