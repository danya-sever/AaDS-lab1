from source.algorithms import has_common_double_binary

print(has_common_double_binary([1, 3, 5], [2, 3, 6]))  # True
print(has_common_double_binary([1, 3, 5], [2, 4, 6]))  # False

print(has_common_double_binary([5], [5]))              # True
print(has_common_double_binary([5], [7]))              # False

print(has_common_double_binary([], [1, 2, 3]))         # False
print(has_common_double_binary([], []))                # False

print(has_common_double_binary([1, 2, 3], [1, 2, 3])) # True
print(has_common_double_binary([1, 5, 10], [2, 7, 10])) # True

print(has_common_double_binary([1, 10], [2, 5, 15, 20])) # False
print(has_common_double_binary([1, 4, 8, 12], [2, 4, 6, 8, 10])) # True