from project.dvd import DVD
from project.customer import Customer


class MovieWorld:
    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10

    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @classmethod
    def dvd_capacity(cls):
        return cls.DVD_CAPACITY

    @classmethod
    def customer_capacity(cls):
        return cls.CUSTOMER_CAPACITY

    def have_capacity_customer(self):
        return len(self.customers) < self.CUSTOMER_CAPACITY

    def have_capacity_dvd(self):
        return len(self.dvds) < self.DVD_CAPACITY

    def add_customer(self, customer: Customer):
        if not self.have_capacity_customer():
            return
        self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if not self.have_capacity_dvd():
            return
        self.dvds.append(dvd)

    def find_customer_by_id(self, customer_id):
        return [customer for customer in self.customers if customer.id == customer_id][0]

    def find_dvd_by_id(self, dvd_id):
        return [dvd for dvd in self.dvds if dvd.id == dvd_id][0]

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = self.find_customer_by_id(customer_id)
        dvd = self.find_dvd_by_id(dvd_id)

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        elif dvd.is_rented:
            return f"DVD is already rented"
        elif customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = self.find_customer_by_id(customer_id)
        dvd = self.find_dvd_by_id(dvd_id)

        if not dvd in customer.rented_dvds:
            return f"{customer.name} does not have that DVD"

        customer.rented_dvds.remove(dvd)
        dvd.is_rented = False
        return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self):
        result = ''

        for customer in self.customers:
            result += f'{customer}\n'

        for dvd in self.dvds:
            result += f'{dvd}\n'

        return result
