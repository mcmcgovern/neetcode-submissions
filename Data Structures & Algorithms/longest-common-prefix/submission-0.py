class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        # iterate over first string, one char at a time
        # check other strings in list to ensure they all have the prefix so far
        for i in range(len(strs[0])):
            # prefix can be max length strs[0]
            # check ith character of each other string in list
            prefix_candidate = strs[0][:i+1]
            confirmed = True
            for list_string in strs[1:]:
                if len(list_string) < i+1:
                    confirmed = False
                    break
                if list_string[i] == prefix_candidate[-1]:
                    continue
                else:
                    confirmed = False
                    break
            if confirmed:
                prefix = prefix_candidate
            else:
                break
        return prefix

