# Create a class called take_skip. Upon initialization it should receive a step (number) and a count (number). Implement the __iter__ and __next__ functions. The iterator should return the count numbers (starting from 0) with the given step. For more clarification, see the examples:

# Test Code:

# numbers = take_skip(2, 6)
# for number in numbers:
#     print(number)

# Desired Output:
# 0
# 2
# 4
# 6
# 8
# 10

class take_skip:
    def __init__(self, step, count):
        self.count = count
        self.step = step

    def __iter__(self):
        self.produced_numbers = 0
        return self

    def __next__(self):
        if self.produced_numbers < self.count:
            temp = self.produced_numbers
            self.produced_numbers += 1
            return self.step * temp
        raise StopIteration()


numbers = take_skip(10, 5)
for number in numbers:
    print(number)
