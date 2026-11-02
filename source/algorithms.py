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

def binary_search_range(a: list[int], target: int, left: int, right: int):

    while left <= right:
        m = (left + right) // 2

        if a[m] == target:
            return True
        if a[m] < target:
            left = m + 1
        else:
            right = m - 1
    return False


def exponential_search(a: list[int], target: int):
    if not a or a[0] >= target:
        return 0

    border = 1

    while border < len(a) and a[border] < target:
        border *= 2

    return border



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


def has_common_binary_search(a: list[int], b: list[int]):
    for i in a:
        if binary_search(b, i):
            return True
    return False

# Time O(M * log(N))
# Memory O(1)

def has_common_exponential_search(a: list[int], b: list[int]):
    if not b:
        return False

    if len(a) > len(b):
        a, b = b, a

    for i in a:
        if b[0] == i:
            return True

        border = exponential_search(b, i)
        left = border // 2
        right = min(border, len(b) - 1)
        if binary_search_range(b, i, left, right):
            return True
    return False

