# Create a class called vowels, which should receive a string. Implement the __iter__ and __next__ methods, so the iterator returns only the vowels from the string.

class vowels:

    def __init__(self, string: str):
        self.string = string
        self.index = 0
        self.vowels_char = ['a', 'e', 'i', 'u', 'y', 'o']
        self.vowels = [el for el in self.string if el.lower() in self.vowels_char]

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.vowels):
            raise StopIteration

        index_to_return = self.index
        self.index += 1

        return self.vowels[index_to_return]

