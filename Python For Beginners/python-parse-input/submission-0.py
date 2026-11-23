from typing import List

def read_integers() -> List[int]:
    user_input = input()
    integer_list = user_input.split(",")
    final_list = []
    for element in integer_list:
        element = int(element)
        final_list.append(element)
    return final_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
