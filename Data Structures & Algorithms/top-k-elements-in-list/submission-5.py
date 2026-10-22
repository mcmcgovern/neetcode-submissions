class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # I'm curious: try default dict with pop
        counts = Counter(nums)
        # most_freq = []

        # for i in range(k):
        #     most_common = counts.most_common()
        #     most_freq.append(most_common)
        #     del counts[most_common]
        # return most_freq
        pairs = counts.most_common(k)
        return [key for key,_ in pairs]