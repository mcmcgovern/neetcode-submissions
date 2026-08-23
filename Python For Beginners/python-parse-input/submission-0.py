from typing import List

def read_integers() -> List[int]:
    user_input = input()
    return [int(num) for num in user_input.split(',')]

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
