class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # ONLY uppercase
        # AT MOST k replacements
        # Use sliding window, advance left when 
        # windowlength - highest_freq <= k
        longest_length = 1
        highest_freq = 0
        count_mapping = defaultdict(int)
        left = 0
        for right, char in enumerate(s):
            count_mapping[char] += 1
            highest_freq = max(highest_freq, count_mapping[char])

            # double check if the current window is valid (fewer than k replacements)
            window_length = right - left + 1
            #print(left, right)
            #print(count_mapping, highest_freq)
            if window_length - highest_freq <= k:
                longest_length = max(longest_length, window_length)
            else:
                while left < right and window_length - highest_freq > k:
                    count_mapping[s[left]] -= 1
                    left += 1
                    window_length = right - left

        return longest_length