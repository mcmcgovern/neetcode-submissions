class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        label = -1

        trust_map = defaultdict(set)
        for i in range(1, n+1):
            trust_map[i] = set()

        for pair in trust:
            person, trusts = pair
            trust_map[person].add(trusts)

        # condition 1: find num in n that has an empty set in trust_map
        candidates = []
        for num in range(1, n+1):
            if num in trust_map:
                print(trust_map[num])
                if len(trust_map[num]) == 0:
                    candidates.append(num)

        # condition 2: check if candidate present in every set
        print(candidates)
        for c in candidates:

            if all(num == c or c in trust_map[num] for num in range(1, n+1)):
                return c
        return label