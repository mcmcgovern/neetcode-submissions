class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # count letters in s1, s2
        # if s2 letters >= s1 True
        s1_counts = defaultdict(int)
        for char in s1:
            s1_counts[char] += 1

        # must be contiguous, a1 bb2
        window_size = len(s1)
        for i in range(len(s2) - window_size + 1):
            s2_window = s2[i:i+window_size]
            print(s2_window)
            window_counts = defaultdict(int)
            for char in s2_window:
                window_counts[char] += 1

            window_match = all([
                letter in window_counts and window_counts[letter] >= count for letter, count in s1_counts.items()
            ])
            # for letter, count in s1_counts.items():
            #     if letter in window_counts and window_counts[letter] >= count:
            #         window_match = True
            #         break

            if window_match:
                return True
        return False
        # s2_counts = defaultdict(int)
        # for char in s2:
        #     s2_counts[char] += 1

        # for letter, count in s1_counts.items():
        #     if letter not in s2_counts:
        #         return False
        #     if s2_counts[letter] < count:
        #         return False

        # return True