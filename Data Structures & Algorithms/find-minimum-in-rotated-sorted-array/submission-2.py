class Solution:
    def findMin(self, nums: List[int]) -> int:
        # the array starts out in sorted order, though it has been rotated
        # rotating the array x times moves the last x elements to the front
        # all nums are unique
        # brute force is trivial min(nums)

        # we know that there are two halves after rotation
        # in both cases the first element of each half may contain the min
        low, high = 0, len(nums)-1
        current_min = nums[0]
        while low <= high:
            mid = low + (high-low) // 2
            print(mid, low, high)
            # what if n[hi] < n[lo]
            if nums[mid] >= current_min:
                low = mid + 1
            else:
                current_min = nums[mid]
                high = mid - 1

        return current_min