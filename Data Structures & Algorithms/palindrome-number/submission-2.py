class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        rev, num = 0, x
        while num > 0:
            last_digit = num % 10
            rev = rev * 10 + last_digit
            num //= 10

        return rev == x