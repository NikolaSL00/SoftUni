class Id:
    def __init__(self):
        self.value_id = 0

    def get_next_id(self):
        self.value_id += 1
        return self.value_id
