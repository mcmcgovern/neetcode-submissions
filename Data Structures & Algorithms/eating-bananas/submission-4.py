class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # try binary search
        low, high = 1, max(piles)
        min_k = high
        while low <= high:
            # try values of k in the middle
            k = low + (high-low) // 2

            hours = 0
            for pile in piles:
                # determine number of hours to eat current pile
                hours += math.ceil(pile / k)

            if hours <= h:
                min_k = min(min_k, k)
                high = k - 1
            else:
                low = k + 1
        return min_k