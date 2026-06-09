class Solution:
    def longestPalindrome(self, s: str) -> str:
        # sliding window
        longest = s[0]
        left, right = 0, 0
        while left < len(s):
            sub = s[left:right+1]
            if self.is_palindrome(sub):
                longest = sub if len(sub) > len(longest) else longest
            right += 1
            if right == len(s):
                left += 1
                right = left
        return longest
        
    def is_palindrome(self, s: str) -> bool:
        return s == s[::-1]