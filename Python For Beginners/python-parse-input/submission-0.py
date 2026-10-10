from typing import List

def read_integers() -> List[int]:
    nums: List[int] = []

    string_list: List[str] = input().split(',')

    for string in string_list:
        nums.append(int(string))
    
    return nums

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
