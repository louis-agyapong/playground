import itertools

my_list = [1, 2, 3]

"""
Combination is the different ways you group something
in which the order doesn't matter.
"""
combination = itertools.combinations(my_list, 3)

# for c in combination:
#     print(c)


"""
Permutation is the different ways you group something
in which the order matters.
"""
permutation = itertools.permutations(my_list, 3)

for p in permutation:
    print(p)
