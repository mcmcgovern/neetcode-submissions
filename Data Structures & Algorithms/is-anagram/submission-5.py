class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s, count_t = defaultdict(int), defaultdict(int)

        for char in s:
            count_s[char] += 1
        for char in t:
            count_t[char] += 1

        for letter in count_s:
            if count_s[letter] != count_t[letter]:
                return False
        for letter in count_t:
            if count_s[letter] != count_t[letter]:
                return False
        return True