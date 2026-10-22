class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # simple solution: sort each
        sorted_groups = defaultdict(list)
        for s in strs:
            s_counts = [0] * 26
            for char in s:
                s_counts[ord(char) - ord('a')] += 1
            # print(s_counts)
            sorted_groups[str(s_counts)].append(s)

        return list(sorted_groups.values())