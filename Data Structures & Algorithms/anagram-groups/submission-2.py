class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # One approach: sort each string and store in a map
        # This map can contain the list of strings that also map to that same sorted sequence of characters

        # groups = {}
        # for s in strs: # n
        #     sorted_s = ''.join(sorted(s)) # mlogm
        #     if sorted_s in groups:
        #         groups[sorted_s].append(s)
        #     else:
        #         groups[sorted_s] = [s]
        # return [group for group in groups.values()]

        # Second approach: parse every string, counting the characters of each
        # Matching char counts will mean anagrams

        groups = defaultdict(list)
        for s in strs:
            counts = [0] * 26
            for char in s:
                counts[ord('a') - ord(char)] += 1
            groups[tuple(counts)].append(s)
        return [group for group in groups.values()]


