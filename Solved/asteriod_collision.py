from typing import List


def asteroidCollision(asteroids: List[int]) -> List[int]:
    collision_stack = []
    for idx, element in enumerate(asteroids):

        # Append when the stack is empty or when the values are all +ve or -ve
        if not collision_stack \
                or (collision_stack[-1] > 0 and element > 0) \
                or (collision_stack[-1] < 0 and element < 0):
            collision_stack.append(element)

        # Operations when last element in stack is -ve
        elif collision_stack[-1] < 0:
            if element > 0:
                collision_stack.append(element)
            if abs(collision_stack[-1]) > abs(element):
                continue
            if abs(collision_stack[-1]) < abs(element):
                collision_stack.pop()
                collision_stack.append(element)
                collision_stack += asteroids[idx + 1:]
                return asteroidCollision(collision_stack)

        # Operations when last element in stack is +ve
        elif collision_stack[-1] > 0:
            if abs(collision_stack[-1]) > abs(element):
                continue
            if abs(collision_stack[-1]) < abs(element):
                collision_stack.pop()
                collision_stack.append(element)
                collision_stack += asteroids[idx + 1:]
                return asteroidCollision(collision_stack)

        # Operation when both are of the same size but moving in different direction
        elif abs(collision_stack[-1]) == abs(element):
            collision_stack.pop()

    return collision_stack


print(asteroidCollision([5, 10, -5]))
print(asteroidCollision([8, -8]))
print(asteroidCollision([10, 2, -5]))
print(asteroidCollision([-2, -1, 1, 2]))
print(asteroidCollision([-2, 1, -2, -2]))