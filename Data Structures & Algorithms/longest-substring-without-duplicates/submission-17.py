class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # map solution
        last_seen = {} # char:last_index
        left = 0
        longest = 0
        for right, char in enumerate(s):
            if char in last_seen:
                left = max(left, last_seen[char] + 1)
            last_seen[char] = right
            longest = max(longest, right - left + 1)
        return longest