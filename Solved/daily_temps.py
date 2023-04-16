from typing import List


# 1st Iteration
# -------------
# def dailyTemperatures(temperatures: List[int]) -> List[int]:
#     res = []
#     counter = 0
#     i, j = 0, 1
#     while j < len(temperatures):
#         if temperatures[j] > temperatures[i]:
#             i += 1
#             j += 1
#             counter += 1
#             res.append(counter)
#             counter = 0
#         elif temperatures[j] < temperatures[i]:
#             j += 1
#             counter += 1
#     return res

# 2nd Iteration
# -------------
def dailyTemperatures(temperatures: List[int]):
    result = [0] * len(temperatures)
    stack = []

    for index, element in enumerate(temperatures):
        while stack and element > stack[-1][0]:
            result[stack[-1][1]] = index - stack[-1][1]
            stack.pop()
        stack.append((element, index))
    return result


# 3rd Iteration - Works but time limit exceeded
# def dailyTemperatures(temperatures: List[int]):
#     i, j = 0, 1
#     count_temps = [0]*len(temperatures)
#     count = 0
#     while j <= len(temperatures) - 1:
#         if temperatures[j] > temperatures[i]:
#             count += 1
#             count_temps[i] = count
#             count = 0
#             i += 1
#             j = i + 1
#         elif temperatures[j] <= temperatures[i]:
#             count += 1
#             j += 1
#             if j == len(temperatures):
#                 count_temps[i] = 0
#                 i += 1
#                 j = i + 1
#                 count = 0
#     count_temps[i] = 0
#     return count_temps


print(dailyTemperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 73]))
print(dailyTemperatures(temperatures=[30, 40, 50, 60]))
print(dailyTemperatures(temperatures=[30, 60, 90]))
# print(dailyTemperatures(temperatures=[89, 62, 70, 58, 47, 47, 46, 76, 100, 70]))
# print(dailyTemperatures(temperatures=[55, 38, 53, 81, 61, 93, 97, 32, 43, 78]))