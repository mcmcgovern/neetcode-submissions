class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1

        # use two pointers to compare each letter starting from both ends of the word
        # advance the pointer if looking at a non-alphanumeric character

        # no need to compare a letter to itself, so < not <=
        while left < right:
            # first skip non-alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            # compare lowercase variants
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True