class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket sort attempt
        freqs = [[] for i in range(len(nums)+1)]
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        for key, value in counts.items():
            freqs[value].append(key)

        result = []
        for i in range(len(freqs)-1, 0, -1):
            for num in freqs[i]:
                result.append(num)
                if len(result) == k:
                    return result