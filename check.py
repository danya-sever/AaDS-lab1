from source.algorithms import (has_common_double_binary,
                               has_common_binary_search,
                               has_common_exponential_search,
                               has_common_two_pointers)

algorithms = [
    ("Два указателя", has_common_two_pointers),
    ("Бинарный поиск", has_common_binary_search),
    ("Экспоненциальный поиск", has_common_exponential_search),
    ("Двойной бинарный", has_common_double_binary)
]

tests = [
    ([1, 2, 3], [3, 4, 5]),                 # True
    ([2, 4, 6], [3, 5, 7]),                 # False
    ([], []),                               # False
    ([-5, -3, 0], [-4, -3, 2]),             # True
    ([1, 3, 5], [2, 4, 6, 8]),              # False
    ([1, 3, 5, 7, 9], [2, 4, 6, 8, 9]),    # True
    ([5], [5]),                             # True
    ([5], [6])                              # False
]

answers = [True, False, False, True, False, True, True, False]

for name, algorithm in algorithms:
    results = []

    for a, b in tests:
        results.append(algorithm(a, b))

    if results == answers:
        print(f"{name}: тест прошел")
    else:
        print(f"{name}: тест не прошел")