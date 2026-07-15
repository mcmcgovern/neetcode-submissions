class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count frequencies of each number
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1

        top_k = set(sorted(freqs.values())[-k::])
        result = []
        for key, val in freqs.items():
            if val in top_k:
                result.append(key)
        return result