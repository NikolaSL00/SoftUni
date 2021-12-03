# Create a class called reverse_iter which should receive an iterable upon initialization. Implement the __iter__ and __next__ methods, so the iterator returns the items of the iterable in reversed order.

# Desired Output:
# 4
# 3
# 2
# 1

class ReverseIterable:
    def __init__(self, iterable_to_reverse):
        self.iterable_to_reverse = iterable_to_reverse
        self.index = len(self.iterable_to_reverse) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration

        index_to_return = self.index
        self.index -= 1
        return self.iterable_to_reverse[index_to_return]


reversed_list = ReverseIterable([1, 2, 3, 4])
for item in reversed_list:
    print(item)
