class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_char_counts = self.count_chars(s)
        t_char_counts = self.count_chars(t)
        return s_char_counts == t_char_counts

    def count_chars(self, string):
        counts = defaultdict(int)
        for char in string:
            counts[char] += 1
        return counts