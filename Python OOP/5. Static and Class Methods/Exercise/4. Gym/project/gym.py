from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.customer import Customer
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer in self.customers:
            return
        self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer in self.trainers:
            return
        self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment in self.equipment:
            return
        self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan in self.plans:
            return
        self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription in self.subscriptions:
            return
        self.subscriptions.append(subscription)

    @staticmethod
    def __get_object_by_id(objects, object_id):
        for object in objects:
            if object.id == object_id:
                return object

    def subscription_info(self, subscription_id):
        subscription = self.__get_object_by_id(self.subscriptions, subscription_id)
        trainer = self.__get_object_by_id(self.trainers, subscription.trainer_id)
        customer = self.__get_object_by_id(self.customers, subscription.customer_id)
        exercise_plan = self.__get_object_by_id(self.plans, subscription.exercise_id)
        equipment = self.__get_object_by_id(self.equipment, exercise_plan.equipment_id)

        result = f'{subscription}\n'
        result += f'{customer}\n'
        result += f'{trainer}\n'
        result += f'{equipment}\n'
        result += f'{exercise_plan}\n'

        return result
