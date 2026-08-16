class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # try hashset solution
        seen = set()
        longest_length = 0
        left = 0
        for right, char in enumerate(s):
            while char in seen:
                seen.remove(s[left])
                left += 1
            seen.add(char)
            longest_length = max(right - left + 1, longest_length)
        return longest_length