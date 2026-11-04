import csv
import os
import time

from source.algorithms import (
    has_common_two_pointers,
    has_common_binary_search,
    has_common_exponential_search,
    has_common_double_binary,
)

ALGORITHMS = {
    "two_pointers": has_common_two_pointers,
    "binary_search": has_common_binary_search,
    "exponential_search": has_common_exponential_search,
    "double_binary_search": has_common_double_binary,
}

TEST_SIZES = [
    ("симметричный_рост", 100, 100),
    ("симметричный_рост", 1000, 1000),
    ("симметричный_рост", 5000, 5000),
    ("симметричный_рост", 10000, 10000),
    ("симметричный_рост", 30000, 30000),
    ("симметричный_рост", 50000, 50000),
    ("симметричный_рост", 100000, 100000),
    ("симметричный_рост", 200000, 200000),
    ("симметричный_рост", 500000, 500000),

    ("фиксированный_м", 50, 200),
    ("фиксированный_м", 50, 500),
    ("фиксированный_м", 50, 2000),
    ("фиксированный_м", 50, 10000),
    ("фиксированный_м", 50, 50000),
    ("фиксированный_м", 50, 200000),
    ("фиксированный_м", 50, 500000),
    ("фиксированный_м", 50, 1000000),
    ("фиксированный_м", 50, 2000000),

    ("изменение_отношения", 100, 100),
    ("изменение_отношения", 100, 500),
    ("изменение_отношения", 100, 1000),
    ("изменение_отношения", 100, 3000),
    ("изменение_отношения", 100, 10000),
    ("изменение_отношения", 100, 50000),
    ("изменение_отношения", 100, 200000),
    ("изменение_отношения", 100, 500000),
]

def generate_arrays(m, n):
    a = [2 * int(i * n / m) + 1 for i in range(m)]
    b = [2 * i for i in range(n)]

    return a, b

def measure_time(algorithm, a, b, repeats=100, batches=5):
    results = []

    for _ in range(batches):
        start = time.perf_counter()
        for _ in range(repeats):
            algorithm(a, b)

        elapsed = time.perf_counter() - start
        results.append(elapsed / repeats)

    results.sort()

    return results[len(results) // 2]


def run_benchmark():
    os.makedirs("data", exist_ok=True)

    with open("data/results.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Тип теста",
            "Размер М",
            "Размер N",
            "Отношение N/M",
            "Алгоритм",
            "Время, с"
        ])

        for test_type, m, n in TEST_SIZES:
            a, b = generate_arrays(m, n)

            print(f"\nТип теста: {test_type}, M={m}, N={n}")

            for name, algorithm in ALGORITHMS.items():
                elapsed = measure_time(algorithm, a, b)

                writer.writerow([
                    test_type,
                    m,
                    n,
                    round(n / m, 4),
                    name,
                    round(elapsed, 8)
                ])

                print(f"{name}: {elapsed:.8f} сек.")


if __name__ == "__main__":
    run_benchmark()