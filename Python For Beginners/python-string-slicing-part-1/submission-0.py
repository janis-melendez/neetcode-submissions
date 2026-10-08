def get_substring(input_string: str, start: int, end: int) -> str:
    substring = ""

    if not (end <= len(input_string)):
        return "" 

    for idx in range(len(input_string)):
        if idx >= start and idx < end:
            substring += input_string[idx]
    
    return substring



# do not modify below this line
print(get_substring("NeetCode", 1, 7))
print(get_substring("NeetCode", 1, 8))
print(get_substring("NeetCode", 1, 9))
print(get_substring("NeetCode", 0, 2))
print(get_substring("NeetCode", 0, 7))
print(get_substring("NeetCode", 4, 8))
