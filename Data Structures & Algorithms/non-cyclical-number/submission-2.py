class Solution:
    
    def isHappy(self, n: int) -> bool:
        seen_sums = set()

        def process(n: int) -> bool:
            # process n: convert to digits and calculate sum
            n_string = str(n)
            print(n_string)
            n_sum = 0
            for char in n_string:
                n_sum += int(char) ** 2

            # check if happy, or if we are in a loop
            if n_sum == 1:
                return True
            elif n_sum in seen_sums:
                return False
            else:
                seen_sums.add(n_sum)

            return process(n_sum)

        return process(n)