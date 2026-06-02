class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda i: i[0])
        merged_intervals = [intervals[0]]
        for start, end in intervals[1:]:
            if start <= merged_intervals[-1][1]:
                # merge
                merged_intervals[-1][1] = max(end, merged_intervals[-1][1])
            else:
                merged_intervals.append([start, end])
        return merged_intervals
