class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # We can count the frequencies of each unique number using a map
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1

        sorted_counts = sorted(freqs.values())
        top_k = set(sorted_counts[-k::])
        result = []
        for key, value in freqs.items():
            if value in top_k:
                result.append(key)

        return result