def add_two_numbers() -> int:
    line = input()
    strings = line.split(',')
    nums = []
    
    for s in strings:
        nums.append(int(s))

    return sum(nums)



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
