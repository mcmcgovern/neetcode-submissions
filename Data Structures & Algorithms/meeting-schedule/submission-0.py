"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # need to sort intervals by start time
        intervals.sort(key=lambda x: x.start)
        # print([(i.start,i.end) for i in intervals])

        for i in range(len(intervals)-1):
            # We need to know if the current meeting ends after the next starts => this would break the condition of no conflicts
            if intervals[i].end > intervals[i+1].start:
                return False

        return True