import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # the two heaviest stones are always chosen
        # continue until 0 or 1 stone is remaining
        num_stones = len(stones)
        max_heap = []
        for stone in stones:
            heapq.heappush_max(max_heap, stone)
        # print(max_heap)
        # print(heapq.heappop_max(max_heap))
        while num_stones > 1:
            print(num_stones)
            # choose two heaviest
            x, y = heapq.heappop_max(max_heap), heapq.heappop_max(max_heap)

            if x == y:
                # destroy both
                # we've already popped so no need to add back on
                num_stones -= 2
            elif x < y:
                heapq.heappush_max(max_heap, y-x)
                num_stones -= 1
            elif x > y:
                heapq.heappush_max(max_heap, x-y)
                num_stones -= 1
        return max_heap[0] if num_stones else 0