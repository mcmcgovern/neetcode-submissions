class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid = []
        for char in s:
            if char.isalnum():
                valid.append(char.lower())
        s = "".join(valid)
        
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True