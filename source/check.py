from source.algorithms import has_common_exponential_search

print(has_common_exponential_search([1, 3, 5], [2, 4, 5]))  # True
print(has_common_exponential_search([1, 3], [2, 4, 6]))      # False
print(has_common_exponential_search([], [1, 2, 3]))          # False