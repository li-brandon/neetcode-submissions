def add_two_numbers() -> int:
    user_input = input()
    number_list = user_input.split(",")
    total = 0
    for number in number_list:
        total += int(number)
    return total

# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
