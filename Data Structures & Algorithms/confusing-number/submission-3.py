class Solution:
    def confusingNumber(self, n: int) -> bool:
        s = str(n)
        rotated = []
        r_mapping = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }
        for i in range(len(s)-1, -1, -1):
            char = s[i]
            if char in ['2', '3', '4', '5', '7']:
                return False

            rotated.append(r_mapping[char])
        print(''.join(rotated))
        return s != ''.join(rotated)