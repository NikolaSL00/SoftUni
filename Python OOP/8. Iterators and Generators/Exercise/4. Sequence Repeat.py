class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.produced = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.produced >= self.number:
            raise StopIteration()
        current = self.produced % len(self.sequence)
        self.produced += 1
        return self.sequence[current]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
