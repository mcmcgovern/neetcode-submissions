class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counts = defaultdict(int)
        t_counts = defaultdict(int)

        for char in s:
            s_counts[char] += 1
        for char in t:
            t_counts[char] += 1

        if len(s_counts.keys()) != len(t_counts.keys()):
            return False

        for key, val in s_counts.items():
            if t_counts[key] != val:
                return False

        return True