from typing import List


def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    all_cars_2 = [(i, j, i + j) for i, j in list(zip(position, speed))]
    print(all_cars_2)
    return 0


carFleet(target=100, position=[0, 2, 4], speed=[4, 2, 1])