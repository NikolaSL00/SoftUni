from project.Id import Id


class Customer:
    id_generator = Id()

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.id = self.get_next_id()

    @staticmethod
    def get_next_id():
        return Customer.id_generator.get_next_id()

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"

