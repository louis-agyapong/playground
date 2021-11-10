import itertools

word = "sample"
my_letters = "plmeas"
print(len(word))

combinations = itertools.combinations(my_letters, len(word))
permutations = itertools.permutations(my_letters, len(word))

for p in permutations:
    print("".join(p))
    if "".join(p) == word:
        print("Match")
        break
    else:
        print("No match")
