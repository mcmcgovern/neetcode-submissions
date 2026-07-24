class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # do brute force first
        result = [0] * len(temperatures) 
        for i in range(len(temperatures)):
            current_temp = temperatures[i]
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > current_temp:
                    result[i] = j - i
                    break
        return result