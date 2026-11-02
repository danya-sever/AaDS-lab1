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