from numbers import Number


class CustomList:
    def __init__(self):
        self.__elements = []
        self.__next_index = 0

    def append(self, value):
        self.__elements.append(value)
        return self.__elements

    def remove(self, index):
        self.validate_index(index)
        return self.__elements.pop(index)

    def get(self, index):
        self.validate_index(index)
        return self.__elements[index]

    def extend(self, iterable):
        new_list = self.copy()
        try:
            iter(iterable)
            for el in iterable:
                new_list.append(el)
        except TypeError:
            new_list.append(iterable)
        return new_list

    def insert(self, idx, value):
        self.validate_index(idx)
        self.__elements.insert(idx, value)
        return self.__elements

    def pop(self):
        if len(self.__elements) == 0:
            raise IndexError('Custom list is empty.')

        return self.__elements.pop()

    def clear(self):
        self.__elements = []

    def first_index(self, value):
        for index in range(len(self.__elements)):
            if self.__elements[index] == value:
                return index
        return -1

    def last_index(self, value):
        for index in range(len(self.__elements) - 1, -1, -1):
            if self.__elements[index] == value:
                return index
        return -1

    def count(self, value):
        count = 0
        for el in self.__elements:
            if el == value:
                count += 1
        return count

    def reverse(self):
        return self.__elements[::-1]

    def copy(self):
        return list(self.__elements)

    def __len__(self):
        return len(self.__elements)

    def add_first(self, value):
        self.insert(0, value)

    def dictionize(self):
        result_dictionary = {}
        last_inserted_key = None

        for index in range(len(self)):
            element = self.get(index)
            if index % 2 == 0:
                result_dictionary[element] = ' '
                last_inserted_key = element
            else:
                result_dictionary[last_inserted_key] = element

        return result_dictionary

    def move(self, amount):
        self.__elements = self.__elements[amount:] + self.__elements[0:amount]
        return self.__elements

    def sum(self):
        sum = 0
        for element in self.__elements:
            if isinstance(element, Number):
                sum += element
            else:
                sum += len(element)
        return sum

    def underbound(self):
        smallest = float('inf')
        smallest_index = -1

        for element in self.__elements:
            if isinstance(element, Number):
                if smallest > element:
                    smallest = element
            else:
                if smallest > len(element):
                    smallest = len(element)

        return self.__elements.index(smallest)

    def overbound(self):
        biggest = float('-inf')
        biggest_index = -1
        for element in self.__elements:
            if isinstance(element, Number):
                if biggest < element:
                    biggest = element
            else:
                if biggest < len(element):
                    biggest = len(element)

        return self.__elements.index(biggest)

    def __iter__(self):
        return self

    def __next__(self):
        if self.__next_index >= len(self):
            self.__next_index = 0
            raise StopIteration

        result = self.__elements[self.__next_index]
        self.__next_index += 1
        return result

    def validate_index(self, index):
        if not isinstance(index, int):
            raise IndexError(f'{index} is not an integer.')
        if index < 0 or index >= len(self.__elements):
            raise IndexError(f'{index} is invalid index')
