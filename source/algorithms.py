def has_common_two_pointers(a: list[int], b: list[int]):
    f = 0
    s = 0

    while f < len(a) and s < len(b):
        if a[f] == b[s]:
            return True
        if a[f] < b[s]:
            f += 1
        else:
            s += 1

    return False

# Time O(M + N)
# Memory O(1)

def binary_search(a: list[int], target: int):
    left = 0
    right = len(a) - 1

    while left <= right:
        m = (left + right) // 2

        if a[m] == target:
            return True
        if a[m] < target:
            left = m + 1
        else:
            right = m - 1
    return False

def has_common_binary_search(a: list[int], b: list[int]):
    for i in a:
        if binary_search(b, i):
            return True
    return False