class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        def is_palindrome(l, r) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        while left < right:
            if s[left] != s[right]:
                return is_palindrome(left+1, right) or is_palindrome(left, right-1)
            left += 1
            right -= 1

        return True



    #     for i in range(len(s)):
    #         if self.is_palindrome(s[:i]+s[i+1:]):
    #             return True
    #     return False

    # def is_palindrome(self, s: str) -> bool:
    #     left, right = 0, len(s) - 1

    #     while left < right:
    #         if s[left] != s[right]:
    #             return False
    #         left += 1
    #         right -= 1
    #     return True