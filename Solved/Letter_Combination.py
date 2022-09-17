import itertools


def letter_combination(digits):
    comb_dict = {"2": ["a", "b", "c"],
                 "3": ["d", "e", "f"],
                 "4": ["g", "h", "i"],
                 "5": ["j", "k", "l"],
                 "6": ["m", "n", "o"],
                 "7": ["p", "q", "r", "s"],
                 "8": ["t", "u", "v"],
                 "9": ["w", "x", "y", "z"]}
    d = [comb_dict[i] for i in digits]
    if not len(digits): return []
    return ["".join(i) if len(i) else [] for i in list(itertools.product(*d))]