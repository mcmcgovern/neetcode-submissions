class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # anagrams: contain same counts of letters
        sorted_strings = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in sorted_strings:
                sorted_strings[sorted_s].append(s)
            else:
                sorted_strings[sorted_s] = [s]

        groups = []
        for key in sorted_strings:
            groups.append(sorted_strings[key])

        return groups