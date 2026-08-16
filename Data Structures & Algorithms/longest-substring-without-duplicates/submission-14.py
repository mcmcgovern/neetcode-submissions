class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # define mapping of chars encountered so far to their last seen index
        substring_chars = defaultdict(int)
        left = 0
        longest_length = 0
        for right, char in enumerate(s):
            if char in substring_chars:
                left = max(left, substring_chars[char] + 1)
            substring_chars[char] = right
            longest_length = max(longest_length, right - left + 1)
        return longest_length