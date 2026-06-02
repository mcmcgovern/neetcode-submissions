class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        matches = []

        words = sorted(words, key=lambda w: len(w))

        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:
                    matches.append(words[i])
                    break

        return matches