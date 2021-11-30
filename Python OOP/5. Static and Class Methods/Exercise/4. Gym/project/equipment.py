from project.Id import Id


class Equipment:
    id_generator = Id()

    def __init__(self, name: str):
        self.name = name
        self.id = self.get_next_id()

    @staticmethod
    def get_next_id():
        return Equipment.id_generator.get_next_id()

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

