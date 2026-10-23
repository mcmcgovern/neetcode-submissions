"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # capture start and end times from intervals
        start_times, end_times = [], []
        for i in intervals:
            start_times.append(i.start)
            end_times.append(i.end)

        # sort both
        start_times.sort()
        end_times.sort()

        # iterate through both lists using two pointers
        # maintain the current min rooms required
        s, e = 0, 0
        min_rooms_needed, num_concurrent_rooms = 0, 0
        while s < len(intervals):
            if start_times[s] < end_times[e]:
                s += 1
                num_concurrent_rooms += 1
            else:
                e += 1
                num_concurrent_rooms -= 1
            min_rooms_needed = max(min_rooms_needed, num_concurrent_rooms)
        return min_rooms_needed





