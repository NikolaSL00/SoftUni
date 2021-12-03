# Create a class called custom_range that receives a start (int) and an end (int) upon initialization. Implement the __iter__ and __next__ methods, so the iterator returns the numbers from the start to the end (inclusive).

# Test Code:
# one_to_ten = custom_range(1, 10)
# for num in one_to_ten:
#     print(num)

# Desired Output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

class CustomRange:
    def __init__(self, start: int, end: int, step: int):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        return CustomRangeIterator(self)


class CustomRangeIterator:
    def __init__(self, custom_range: CustomRange):
        self.custom_range = custom_range
        self.current_number = self.custom_range.start
        self.step = custom_range.step

    def __next__(self):
        if (self.step > 0 and self.custom_range.end < self.current_number) \
                or (self.step < 0 and self.custom_range.end > self.current_number):
            raise StopIteration

        value_to_return = self.current_number
        self.current_number += self.step
        return value_to_return


one_to_ten = CustomRange(100, 10, -15)
for num in one_to_ten:
    print(num)
