class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # index preservation is not required -> definitely sort...
        nums.sort()
        # imagine [-4,-1,-1,0,1,2]
        triplets = []
        seen = set()
        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1
            while left < right:
                a,b,c = nums[i], nums[left], nums[right]
                if a+b+c == 0:
                    triplet_hash = f'{a}#{b}#{c}'
                    # print(triplet_hash)
                    # print(list(seen))
                    if triplet_hash not in seen:
                        triplets.append([a,b,c])
                        seen.add(triplet_hash)
                    left+=1
                elif a+b+c < 0:
                    left+=1
                else:
                    right-=1


        return triplets


























        # brute force
        # seen = set()
        # triplets = []
        # for i in range(len(nums)-2):
        #     for j in range(i+1, len(nums)-1):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 sorted_triplet = sorted([nums[i],nums[j],nums[k]])
        #                 triplet_hash = '#'.join([str(t) for t in sorted_triplet])
        #                 if triplet_hash not in seen:
        #                     seen.add(triplet_hash)
        #                     triplets.append(sorted_triplet)


        # return triplets