class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # simple solution: sort each
        sorted_groups = defaultdict(list)
        for s in strs:
            sorted_s = str(sorted(s))
            sorted_groups[sorted_s].append(s)

        return list(sorted_groups.values())