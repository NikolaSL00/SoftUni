class Room:
    def __init__(self, number: int, capacity: int):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    @staticmethod
    def cant_take_room(is_taken, capacity, people):
        return is_taken or capacity < people

    def take_room(self, people):
        if self.cant_take_room(self.is_taken, self.capacity, people):
            return f"Room number {self.number} cannot be taken"
        self.guests = people
        self.is_taken = True

    def free_room(self):
        if self.is_taken:
            self.is_taken = False
            self.guests = 0
            return
        return f"Room number {self.number} is not taken"
