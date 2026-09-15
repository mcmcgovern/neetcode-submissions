class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        # if even, take average
        self.nums.sort()
        l = len(self.nums)
        mid = l // 2
        if l % 2 == 0:
            return (self.nums[mid] + self.nums[mid - 1]) / 2
        else:
            return self.nums[mid]