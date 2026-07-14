class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # One approach: sort each string and store in a map
        # This map can contain the list of strings that also map to that same sorted sequence of characters

        groups = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in groups:
                groups[sorted_s].append(s)
            else:
                groups[sorted_s] = [s]
        return [group for group in groups.values()]

        