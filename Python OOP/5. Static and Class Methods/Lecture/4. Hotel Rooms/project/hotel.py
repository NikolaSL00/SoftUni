from project.room import Room


class Hotel:

    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_room_by_number(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                return room

    def take_room(self, room_number, people):
        room = self.get_room_by_number(room_number)

        if Room.cant_take_room(room.is_taken, room.capacity, people):
            return

        room.take_room(people)
        self.guests += people

    def free_room(self, room_number):
        room = self.get_room_by_number(room_number)

        self.guests -= room.guests
        room.free_room()

    def status(self):
        result = f"Hotel {self.name} has {self.guests} total guests\n"
        result += f'Free rooms: {", ".join([str(room.number) for room in self.rooms if not room.is_taken])}\n'
        result += f'Taken rooms: {", ".join([str(room.number) for room in self.rooms if room.is_taken])}'
        return result
