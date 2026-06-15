class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find partition, do binary search
        low, high = 0, len(nums)-1
        # [5,6,1,2,3,4]
        partition = 0
        while low < high:
            mid = (low+high)//2
            if nums[mid] > nums[low] and nums[mid] > nums[high]:
                if partition == mid:
                    break
                low = mid
                partition = low
            else:
                high = mid
        print(partition)
        
        # after finding partition, we can search in two halves of array
        low, high = 0, partition
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        # if the larger half doesn't have it check the smaller
        low, high = partition+1, len(nums)-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1