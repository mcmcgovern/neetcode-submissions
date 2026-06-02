class Solution:
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s)):
            if self.is_palindrome(s[:i]+s[i+1:]):
                return True
        return False

    def is_palindrome(self, s: str) -> bool:
        return s == s[::-1]