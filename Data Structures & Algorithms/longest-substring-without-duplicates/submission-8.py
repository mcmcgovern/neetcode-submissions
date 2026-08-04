class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        longest = 1
        unique = set(s[0])
        left = 0
        for i in range(1, len(s)):
            # it is possible char is already in the window set
            if s[i] not in unique:
                unique.add(s[i])
            else:
                while left < i and s[i] in unique:
                    # print(s[left])
                    unique.remove(s[left])
                    left += 1
                unique.add(s[i])
            longest = max(longest, i - left + 1)
        return longest