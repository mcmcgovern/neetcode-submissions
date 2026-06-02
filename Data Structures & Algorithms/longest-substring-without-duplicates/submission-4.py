class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        # Set up sliding window with set of currently seen chars
        left, right = 0, 1
        seen = set(s[left])
        longest_length = 1
        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                longest_length = max(longest_length, len(seen))
                right += 1
            else:
                while s[right] in seen:
                    seen.remove(s[left])
                    left += 1

        return longest_length