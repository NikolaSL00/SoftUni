# Create a generator function called possible_permutations() which should receive a list and return lists with all possible permutations between it's elements.


# Test Code:
# [print(n) for n in possible_permutations([1, 2, 3])]

# Desired Output:
# [1, 2, 3]
# [1, 3, 2]
# [2, 1, 3]
# [2, 3, 1]
# [3, 1, 2]
# [3, 2, 1]

def all_permutations(seq):
    if len(seq) == 0:
        return []

    if len(seq) == 1:
        return [seq]

    l = []
    for i in range(len(seq)):
        m = seq[i]

        remove_last = seq[:i] + seq[i + 1:]

        for p in all_permutations(remove_last):
            l.append([m] + p)
    return l


def possible_permutations(seq):
    perms = all_permutations(seq)
    for perm in perms:
        yield perm


[print(n) for n in possible_permutations([1, 2, 3])]
