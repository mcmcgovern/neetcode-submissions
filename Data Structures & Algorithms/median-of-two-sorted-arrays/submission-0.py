class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # simple solution is to combine arrays, sort them, and return middle
        combined = nums1+nums2
        combined.sort()
        print(combined)
        if len(combined) == 1:
            return combined[0]
        elif len(combined) % 2 == 0:
            # perform division
            midpoint = len(combined) // 2
            m1, m2 = combined[midpoint], combined[midpoint-1]
            return (m1+m2) / 2
        else:
            return combined[len(combined) // 2]