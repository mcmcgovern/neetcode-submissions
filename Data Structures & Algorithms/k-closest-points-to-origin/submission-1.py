import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # origin is a point: 0,0
        # k is heap size
        # we want to minimize distance, so use min heap
        min_heap = []
        for p in points:
            distance = self.calc_distance(p)
            heapq.heappush_max(min_heap, (distance, p))
            if len(min_heap) > k:
                heapq.heappop_max(min_heap)

        return [point for (dist, point) in min_heap]
        
    def calc_distance(self, p: tuple) -> float:
        x1, y1 = p
        x2, y2 = 0, 0
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)