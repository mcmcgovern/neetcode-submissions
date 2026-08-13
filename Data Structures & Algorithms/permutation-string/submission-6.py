class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # only lowercase letters
        # again we are dealing with character counts (or sorting strings)
        if len(s1) > len(s2):
            return False

        # counts of s1 are always relevant and unchanging
        # fixed sliding window will be performed on s2
        window_size = len(s1)
        s1_sorted = sorted(s1)
        for i in range(len(s2)):
            part = s2[i:i+window_size]
            # print(s1, part)
            if s1_sorted == sorted(part):
                return True
        return False