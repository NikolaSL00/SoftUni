number_to_month = {
    '01': 'Janauary',
    '02': 'February',
    '03': 'March',
    '04': 'April',
    '05': 'May',
    '06': 'June',
    '07': 'July',
    '08': 'August',
    '09': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December'
}


class DVD:
    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        day, month, year = date.split('.')
        month = number_to_month[month]
        return cls(name, id, int(year), month, age_restriction)

    def rented_or_not_str(self):
        if self.is_rented:
            return 'rented'
        return 'not rented'

    def __repr__(self):
        result = self.rented_or_not_str()
        return f'{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {result}'
