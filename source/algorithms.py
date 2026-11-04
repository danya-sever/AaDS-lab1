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


def insert_position(a: list[int], target: int, left: int = 0, right: int = None):
    if right is None:
        right = len(a)

    while left < right:
        m = (left + right) // 2

        if a[m] < target:
            left = m + 1
        else:
            right = m

    return left

"Два указателя"
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

"Бинарный поиск"
def has_common_binary_search(a: list[int], b: list[int]):
    for i in a:
        if binary_search(b, i):
            return True
    return False

# Time O(M * log(N))
# Memory O(1)

"Экспоненциальный поиск"
def has_common_exponential_search(a: list[int], b: list[int]):
    if not b:
        return False

    if len(a) > len(b):
        a, b = b, a

    j = 0

    for i in a:
        if j >= len(b):
            return False
        if b[j] == i:
            return True
        if b[j] > i:
            continue

        border = 1

        while j + border < len(b) and b[j + border] < i:
            border *= 2

        left = j + border // 2 - 1
        right = min(j + border, len(b) - 1) + 1

        while right - left > 1:
            m = (left + right) // 2
            if b[m] == i:
                return True
            elif b[m] > i:
                right = m
            else:
                left = m
        j = right
    return False


# Time O(M * log(2N/M))
# Memory O(1)

"Двойной бинарный"
def has_common_double_binary(a: list[int], b: list[int]):
    if len(a) > len(b):
        a, b = b, a

    def search(la: int, ra: int, lb: int, rb: int):
        if la >= ra or lb >= rb:
            return False
        m = (la + ra) // 2
        val = a[m]
        pos = insert_position(b, val, lb, rb)
        if pos < rb and b[pos] == val:
            return True
        return (search(la, m, lb, pos) or search(m + 1, ra, pos, rb))

    return search(0, len(a), 0, len(b))





