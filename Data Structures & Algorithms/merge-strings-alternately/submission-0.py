class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""

        index = 0
        while index < len(word1) and index < len(word2):
            merged += f'{word1[index]}{word2[index]}'
            index += 1

        if index < len(word1):
            merged += word1[index:]
        elif index < len(word2):
            merged += word2[index:]

        return merged