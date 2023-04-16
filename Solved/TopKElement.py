from collections import Counter


def solution(arr, k):
    """
    Given an integer array nums and an integer k, return the k most frequent elements.
    You may return the answer in any order.
    :param arr: List[Int]
    :param k: Int
    :return: List[Int]
    """
    # Method 1 -> This solution is not optimized and inefficient
    # arr_dict = {i: arr.count(i) for i in arr}
    # return [i for i, j in sorted(arr_dict.items(), key=lambda x: x[1], reverse=True)][:k]  # O(n)


def solution_2(arr, k):
    # Method 2 - O(log n) is optimized and efficient
    most_common = Counter(arr).most_common()
    print(most_common)
    return [i for i, j in most_common[:k]]


print(solution_2([5, 3, 1, 1, 1, 3, 73, 1], 1))