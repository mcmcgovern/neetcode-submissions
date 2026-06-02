class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # triplets = set()
        # return list(triplets)

        # brute force
        seen = set()
        triplets = []
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        sorted_triplet = sorted([nums[i],nums[j],nums[k]])
                        triplet_hash = '#'.join([str(t) for t in sorted_triplet])
                        if triplet_hash not in seen:
                            seen.add(triplet_hash)
                            triplets.append(sorted_triplet)


        return triplets