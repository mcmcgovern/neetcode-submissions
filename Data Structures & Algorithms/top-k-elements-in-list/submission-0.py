class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)

        for num in nums:
            freqs[num] += 1

        # create a sorted copy of freqs
        k_highest = sorted(list(freqs.values()), reverse=True)[:k]

        top = []
        for num, freq in freqs.items():
            if freq in k_highest:
                top.append(num)
        return top