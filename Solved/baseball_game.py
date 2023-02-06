from typing import List


def calPoints(operations: List[str]):
    my_stack = []

    for i in operations:
        match i:
            case 'C':
                my_stack.pop()
            case 'D':
                my_stack.append(int(my_stack[-1]) * 2)
            case '+':
                my_stack.append(int(my_stack[-1]) + int(my_stack[-2]))
            case _:
                my_stack.append(int(i))

    return sum(my_stack)


print(calPoints(["5", "2", "C", "D", "+"]))