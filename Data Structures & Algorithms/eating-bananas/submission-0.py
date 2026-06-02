class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        min_speed = right
        while left <= right:
            mid = (left+right) // 2
            if self.try_eating_rate(mid, h, piles):
                min_speed = mid
                right = mid - 1
            else:
                left = mid + 1
        return min_speed
            
    def try_eating_rate(self, rate: int, hours: int, piles: list[int]) -> bool:
        total_hours = 0
        for pile in piles:
            total_hours += math.ceil(pile / rate)
            if total_hours > hours:
                return False
        return total_hours <= hours




