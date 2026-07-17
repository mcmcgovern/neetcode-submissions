class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # define tuples representing counts of each alphabet letter
        groups = defaultdict(list)
        for s in strs:
            counts = [0] * 26
            for char in s:
                counts[ord('a')-ord(char)] += 1
            groups[tuple(counts)].append(s)
        return list(groups.values())