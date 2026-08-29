class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # use binary search, in range 1 to max(piles) to represent eating rates
        low, high = 1, max(piles)
        min_speed = high # we know for sure that the largest pile will work as a maximum rate over the given number of hours

        while low <= high:
            k = low + (high-low) // 2

            # we can now test our midpoint as an eating speed
            hours = 0
            for p in piles:
                # calculate number of hours it would take to eat
                # current pile (rounded up since we can eat max 1 pile)
                hours += math.ceil(p / k)

            # we need to check if we ran out of time, if so increase speed
            if hours > h:
                low = k + 1
            else:
                # otherwise, we have eaten all bananas
                # we should update our current min_speed and see if 
                # smaller is possible
                min_speed = min(min_speed, k)
                high = k - 1
        return min_speed