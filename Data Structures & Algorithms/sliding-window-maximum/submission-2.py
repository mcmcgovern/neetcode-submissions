class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window_maxes = []
        queue = deque() # keep track of indexes
        left = 0
        for right in range(len(nums)):
            # first pop smaller values from queue
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()
            queue.append(right)

            # remove left from window
            if left > queue[0]:
                queue.popleft()

            # begin adding the window max after k values 
            # have been evaluated
            if (right + 1) >= k:
                window_maxes.append(nums[queue[0]])
                left += 1

        return window_maxes