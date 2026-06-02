class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 1:
            return 1
        last_length = 0
        last_index = -1
        for i in range(len(s)-1, -1, -1):
            if last_index == -1 and s[i] != ' ':
                last_index = i
            elif last_index != -1 and s[i] == ' ':
                # found beginning of word
                return last_index - i
        # return len(s.strip().split(' ')[-1])