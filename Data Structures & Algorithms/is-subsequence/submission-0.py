class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer = 0

        for char in t:
            if s_pointer < len(s) and char == s[s_pointer]:
                s_pointer += 1

        return s_pointer == len(s)