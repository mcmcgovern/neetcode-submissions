class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # simple solution is to combine arrays, sort them, and return middle
        combined = nums1+nums2
        combined.sort()
        midpoint = len(combined) // 2
        if len(combined) == 1:
            return combined[0]
        elif len(combined) % 2 == 0:
            # perform division
            m1, m2 = combined[midpoint], combined[midpoint-1]
            return (m1+m2) / 2
        else:
            return combined[midpoint]