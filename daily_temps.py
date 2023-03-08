from typing import List


# 2nd Iteration
# -------------
def dailyTemperatures_II(temperatures: List[int]):
    result = [0] * len(temperatures)
    stack = []

    for index, element in enumerate(temperatures):
        while stack and element > stack[-1][0]:
            result[stack[-1][1]] = index - stack[-1][1]
            stack.pop()
        stack.append((element, index))
    return result


# 3rd Iteration - Works but time limit exceeded
def dailyTemperatures(temperatures: List[int]):
    i, j = 0, 1
    count_temps = [0]*len(temperatures)
    count = 0
    while j <= len(temperatures) - 1:
        if temperatures[j] > temperatures[i]:
            count += 1
            count_temps[i] = count
            count = 0
            i += 1
            j = i + 1
        elif temperatures[j] <= temperatures[i]:
            count += 1
            j += 1
            if j == len(temperatures):
                count_temps[i] = 0
                i += 1
                j = i + 1
                count = 0
    count_temps[i] = 0
    return count_temps


print(dailyTemperatures_II(temperatures=[73, 74, 75, 71, 69, 72, 76, 73]))
print(dailyTemperatures_II(temperatures=[30, 40, 50, 60]))
print(dailyTemperatures_II(temperatures=[30, 60, 90]))
print(dailyTemperatures(temperatures=[89, 62, 70, 58, 47, 47, 46, 76, 100, 70]))
print(dailyTemperatures(temperatures=[55, 38, 53, 81, 61, 93, 97, 32, 43, 78]))