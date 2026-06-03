class Solution:
    def romanToInt(self, s: str) -> int:
        numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        result = 0
        for i in range(len(s)):
            if i + 1 < len(s) and numerals[s[i]] < numerals[s[i+1]]:
                result -= numerals[s[i]]
            else:
                result += numerals[s[i]]
        return result