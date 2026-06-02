class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            square_sum = self.sum_square_of_digits(n)
            if square_sum == 1:
                return True
            print(seen)
            n = square_sum
        return False
        

    def sum_square_of_digits(self, n: int) -> int:
        result = 0
        while n >= 10:
            digit = n % 10
            result += (digit ** 2)
            print(digit, result, n)
            n //= 10
        return result + ((n % 10) ** 2)