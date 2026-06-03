class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        # iterate over first string, one char at a time
        # check other strings in list to ensure they all have the prefix so far
        for i in range(len(strs[0])):
            # prefix can be max length strs[0]
            # check ith character of each other string in list
            prefix_char = strs[0][i]
            confirmed = True
            for list_string in strs[1:]:
                if len(list_string) < i+1 or list_string[i] != prefix_char:
                    confirmed = False
                    break
                if list_string[i] == prefix_char:
                    continue

            if confirmed:
                prefix = strs[0][:i+1]
            else:
                break
        return prefix

