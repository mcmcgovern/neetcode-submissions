def concatenate(s1: str, s2: str) -> str:
    combined = s1 + s2
    return combined if len(combined) <= 10 else 'Too long!'




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
