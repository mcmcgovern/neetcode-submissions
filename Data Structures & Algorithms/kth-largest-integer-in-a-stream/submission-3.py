import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.largest_nums = heapq.nlargest(k, nums)
        self.k = k

    def add(self, val: int) -> int:
        self.largest_nums.append(val)
        self.largest_nums = heapq.nlargest(self.k, self.largest_nums)
        return self.largest_nums[-1]