class Solution:
    def isPalindrome(self, s: str) -> bool:
        s="".join(s.lower() for s in s if s.isalnum())
        for i in range(len(s)):
            if s[i]!=s[len(s)-i-1]:
                return False
        return True


