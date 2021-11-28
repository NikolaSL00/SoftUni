from project.food import Food


class Fruit(Food):

    def __init__(self, name, expiration_date):
        super(Fruit, self).__init__(expiration_date)
        self.name = name
