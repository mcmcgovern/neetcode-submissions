class Solution:

    def encode(self, strs: List[str]) -> str:
        # length of string followed by string followed by next length, etc
        result = ""
        for s in strs:
            result += f'{len(s)}#{s}'
        return result

    def decode(self, s: str) -> List[str]:
        print(s)
        result = []
        i = 0
        while i < len(s):
            # next char should be a length specification, could be multiple digits
            start = i
            while s[i].isdigit():
                i += 1
            length = int(s[start:i])
            i += 1
            result.append(s[i:i+length])
            i += length
        return result