class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sorting each string can create a key we can use to map them to each other
        groups = defaultdict(list)
        for s in strs:
            sorted_s = sorted(s)
            groups[''.join(sorted_s)].append(s)

        return list(groups.values())