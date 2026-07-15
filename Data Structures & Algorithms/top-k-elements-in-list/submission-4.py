class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # The frequency for each num in nums can only be between 1-N
        # Thus we can reserve slots between 0-N+1 to hold counts of each num
        freqs = [[] for i in range(0, len(nums)+1)]
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        # print(counts)
        for num, count in counts.items():
            freqs[count].append(num)
            # print(freqs)

        # iterate backwards until we run out of k
        # print(freqs)
        result = []
        i = -1
        while k > 0:
            freq = freqs[i]
            for num in freq:
                result.append(num)
                k -= 1
                if k == 0:
                    return result
            i -= 1
        return result