class Integer:

    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @staticmethod
    def is_float(number):
        return isinstance(number, float)

    @staticmethod
    def is_numeric(string: str):
        return isinstance(string, str) and all([True for el in string if el.isnumeric()])

    @classmethod
    def from_float(cls, float_value):
        if not cls.is_float(float_value):
            return f"value is not a float"
        return cls(int(float_value))

    @classmethod
    def from_roman_to_int(cls, value):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
                 'CD': 400, 'CM': 900}
        i = 0
        num = 0
        while i < len(value):
            if i + 1 < len(value) and value[i:i + 2] in roman:
                num += roman[value[i:i + 2]]
                i += 2
            else:
                # print(i)
                num += roman[value[i]]
                i += 1
        return num

    @classmethod
    def from_roman(cls, roman_value):
        return cls(cls.from_roman_to_int(roman_value))

    @classmethod
    def from_string(cls, string_value):
        if not cls.is_numeric(string_value):
            return "wrong type"
        return cls(int(string_value))


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
