import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.num_stream = nums
        self.k = k
        heapq.nlargest(k, nums)
        self.largest_nums = nums

    def add(self, val: int) -> int:
        # we know one must be popped to retain k elements
        self.num_stream.append(val)
        self.largest_nums = self.num_stream
        self.largest_nums = heapq.nlargest(self.k, self.num_stream)
        return self.largest_nums[-1]