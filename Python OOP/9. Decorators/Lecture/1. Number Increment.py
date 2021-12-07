# Having the following code:
# print(number_increment([1, 2, 3]))

# Complete the code so it works as expected:
# [2, 3, 4]


def number_increment(param):
    def increase():
        return [x + 1 for x in param]

    return increase()


print(number_increment([1, 2, 3]))
