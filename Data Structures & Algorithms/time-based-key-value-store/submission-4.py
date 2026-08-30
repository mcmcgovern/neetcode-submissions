class TimeMap:

    def __init__(self):
        self.mapping = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mapping:
            self.mapping[key] = []
        self.mapping[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        values = self.mapping.get(key, [])

        # binary search
        low, high = 0, len(values)-1
        while low <= high:
            mid = low + (high-low) // 2
            if values[mid][1] == timestamp:
                return values[mid][0]
            elif values[mid][1] < timestamp:
                result = values[mid][0]
                low = mid + 1
            else:
                high = mid - 1
        return result