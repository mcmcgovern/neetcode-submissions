class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ''
        encoded = ""
        for s in strs:
            encoded += f'{len(s)}#{s}'
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        decoded = []
        index = 0
        while index < len(s):
            start = index

            # get all digits of length
            while s[index] != "#":
                index += 1

            # we know the next char is #

            length = int(s[start:index])

            decoded.append(s[index+1:index+1+length])
            index += length+1

        return decoded