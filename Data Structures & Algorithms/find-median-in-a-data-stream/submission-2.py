class MedianFinder:

    def __init__(self):
        self.small_half, self.large_half = [], [] # max_heap, min_heap

    def addNum(self, num: int) -> None:
        # is num larger than the smallest in large half
        if self.large_half and num > self.large_half[0]:
            heapq.heappush(self.large_half, num)
        else:
            heapq.heappush_max(self.small_half, num)

        # are the two halves off balance
        if len(self.small_half) > len(self.large_half) + 1:
            heapq.heappush(self.large_half, heapq.heappop_max(self.small_half))
        if len(self.large_half) > len(self.small_half) + 1:
            heapq.heappush_max(self.small_half, heapq.heappop(self.large_half))
        

    def findMedian(self) -> float:
        if len(self.small_half) > len(self.large_half):
            return self.small_half[0]
        if len(self.large_half) > len(self.small_half):
            return self.large_half[0]

        # if they are equal, take average
        return (self.small_half[0] + self.large_half[0]) / 2