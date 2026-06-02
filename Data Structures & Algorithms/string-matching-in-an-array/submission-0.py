class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        matches = set()

        for i in range(len(words)):
            for j in range(len(words)):
                # if i != j and self.is_substring(words[i], words[j]):
                if i != j and words[j].find(words[i]) != -1:
                    matches.add(words[i])

        return list(matches)

    # def is_substring(self, a, b):
    #     a_pointer = 0

    #     for i in range(len(b)):
    #         if a_pointer < len(a) and a[a_pointer] == b[i]:
    #             a_pointer += 1

    #     return a_pointer == len(a)