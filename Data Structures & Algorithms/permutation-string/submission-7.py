class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # only lowercase letters
        # again we are dealing with character counts (or sorting strings)
        if len(s1) > len(s2):
            return False

        # counts of s1 are always relevant and unchanging
        # fixed sliding window will be performed on s2
        window_size = len(s1)
        s1_counts = [0] * 26
        for char in s1:
            s1_counts[ord(char) - ord('a')] += 1

        window_counts = [0] * 26
        for i in range(len(s2)):
            char = s2[i]
            if i < window_size:
                window_counts[ord(char) - ord('a')] += 1
            else:
                # decrement char we are removing from window
                # resulting window will be: i, i-1, i-2
                window_counts[ord(s2[i-window_size]) - ord('a')] -= 1
                window_counts[ord(char) - ord('a')] += 1
            
            print(char, s1_counts, window_counts)
            if s1_counts == window_counts:
                return True
        return False