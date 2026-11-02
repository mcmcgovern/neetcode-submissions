class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # one way is: Counter
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        freqs = sorted(list(counts.values()), reverse=True)
        k_freqs = set(freqs[:k])

        top_k = []
        for num, freq in counts.items():
            if freq in k_freqs:
                top_k.append(num)

        return top_k