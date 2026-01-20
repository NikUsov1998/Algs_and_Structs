def strings_equals(text: str, substring: str, i: int) -> int:
    return substring == text[i:i+len(substring)]


def substring_search(text: str, substring: str) -> list[int]:
    result: list[int] = []
    for i in range(len(text)-len(substring)):
        if strings_equals(text, substring, i):
            result.append(i)
    return result


text: str = "Little cat, little cat, i have no a flat."
substring: str = "cat"
s = substring_search(text, substring)
print(s)
