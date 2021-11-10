import itertools

my_list = [1, 2, 3, 4, 5, 6]

combination = itertools.combinations(my_list, 3)

"""How many different groups of 3 from the list are equal to 10."""

print([result for result in combination if sum(result) == 10])
