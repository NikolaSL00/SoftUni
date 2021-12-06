class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dictionary = dictionary

    def __iter__(self):
        self.dictionary_elements = list(self.dictionary.items())
        self.current_index = 0
        return self

    def __next__(self):
        if self.current_index == len(self.dictionary_elements):
            raise StopIteration
        temp = self.current_index
        self.current_index += 1
        return self.dictionary_elements[temp]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
