import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    sorted_nums = []
    for num in nums:
        pair = (-num, num)
        heapq.heappush(sorted_nums, pair)
    return [n for (p,n) in sorted(sorted_nums)]



# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
