import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # the two heaviest stones are always chosen
        # continue until 0 or 1 stone is remaining
        heapq.heapify_max(stones)
        while len(stones) > 1:
            # choose two heaviest
            x, y = heapq.heappop_max(stones), heapq.heappop_max(stones)

            if x == y:
                # destroy both
                # we've already popped so no need to add back on
                continue
            elif x < y:
                heapq.heappush_max(stones, y-x)
            elif x > y:
                heapq.heappush_max(stones, x-y)
        return stones[0] if len(stones) else 0